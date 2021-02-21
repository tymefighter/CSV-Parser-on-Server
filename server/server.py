import os
import pandas as pd
from flask import Flask, request, send_file, jsonify
from metadata import MetadataDict, Metadata

HOST = '127.0.0.1'
PORT = '5000'

app = Flask(__name__)
file_metadata = MetadataDict()

@app.route('/upload', methods=['POST'])
def handle_file_upload_request():

    uploaded_file = request.files['file']
    uploaded_file.save(uploaded_file.filename)

    file_metadata.store(
        uploaded_file.filename,
        Metadata(uploaded_file.filename)
    )


@app.route('/filelist', methods=['GET'])
def handle_file_list_request():

    return jsonify(list(filter(
        lambda filename: filename.endswith('.csv'),
        os.listdir()
    )))


@app.route('/metadata', methods=['GET'])
def handle_file_metadata_request():

    filename = request.args.get('filename')
    print(file_metadata.metadata_dict.keys())
    return file_metadata\
        .get(filename)\
        .to_dict()


@app.route('/query', methods=['GET'])
def handle_query_request():

    filename = request.args.get('filename')
    start_row = int(request.args.get('start_row'))
    num_rows = int(request.args.get('num_rows'))

    temp_file_name = f'_meta_{start_row}_{num_rows}_{filename}'
    pd.read_csv(filename, skiprows=start_row, nrows=num_rows)\
        .to_csv(temp_file_name, index=False)

    return_val = send_file(temp_file_name)
    os.remove(temp_file_name)

    return return_val


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
