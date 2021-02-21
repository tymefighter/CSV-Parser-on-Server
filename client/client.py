from client_requests import \
    upload_csv, request_file_list, request_file_metadata, query_for_rows

from client_display import \
    display_file_list, display_file_metadata, display_rows


def main():

    print(
        'Information ---\n'
        + 'upload <filename> -> upload csv file to the server\n'
        + 'filelist -> request file list from the server\n'
        + 'metadata <filename> -> request file metadata from the server\n'
        + 'query <filename> <start row> <num rows> -> query for rows of'
        + 'the csv file specified\n'
        + 'quit - quit the program'
    )

    while True:

        user_input = input().split()

        if user_input[0] == 'upload':
            upload_csv(user_input[1])

        elif user_input[0] == 'filelist':
            file_list = request_file_list()
            display_file_list(file_list)

        elif user_input[0] == 'metadata':
            metadata = request_file_metadata(user_input[1])
            display_file_metadata(metadata)

        elif user_input[0] == 'query':
            filename = query_for_rows(
                filename=user_input[1],
                start_row=int(user_input[2]),
                num_rows=int(user_input[3])
            )
            display_rows(filename)

        elif user_input[0] == 'quit':
            break

        else:
            print('Invalid Input')

if __name__ == '__main__':
    main()
