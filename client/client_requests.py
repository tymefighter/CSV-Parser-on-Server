import requests
import os

SERVER_ADDRESS = 'http://127.0.0.1:5000'


def upload_csv(filepath):
    """
    Upload CSV file to the server

    :param filepath: path to the file which is to be uploaded to the server
    :return: None
    """

    upload_file_address = SERVER_ADDRESS + '/upload'
    requests.post(upload_file_address, files={
        'file': (os.path.split(filepath)[-1], open(filepath, 'rb'))
    })


def request_file_list():
    """
    Request for the list of csv files present at
    the server

    :return: list of filenames i.e. python list of strings
    """

    file_list_address = SERVER_ADDRESS + '/filelist'
    file_list = requests.get(file_list_address).json()

    return file_list


def request_file_metadata(filename):
    """
    Request for metadata of the provided filename

    :param filename: name of the file whose metadata is to be requested
    :return: python dictionary containing the metadata of the file
    """

    metadata_address = SERVER_ADDRESS + '/metadata'
    metadata = requests\
        .get(metadata_address, params={'filename': filename})\
        .json()

    return metadata


def query_for_rows(filename, start_row, num_rows):

    query_address = SERVER_ADDRESS + '/query'
    response = requests.get(
        query_address, 
        params={
            'filename': filename, 
            'start_row': start_row, 
            'num_rows': num_rows
        }
    )

    with open(filename, 'wb') as fl:
        fl.write(response.content)

    return filename
