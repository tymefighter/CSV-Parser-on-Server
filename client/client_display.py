import pandas as pd
import matplotlib.pyplot as plt


def display_file_list(file_list):
    """
    Displays list of filename string provided
    as input

    :param file_list: list of filename strings
    :return: None
    """

    print('Server File List: ')

    for filename in file_list:
        print(filename)


def display_file_metadata(metadata):
    """
    Displays the provided metadata information

    :param metadata: metadata of a file
    :return: None
    """

    print(
        f'filename: {metadata["filename"]}\n'
        + f'number of rows: {metadata["num_rows"]}\n'
        + f'number of cols: {len(metadata["column_names"])}\n'
        + f'column names:'
    )

    for column_name in metadata["column_names"]:
        print(column_name)


def display_rows(filename):

    df = pd.read_csv(filename)

    axes = plt.gca()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    plt.box(on=None)

    table = plt.table(
        cellText=df.to_numpy(), loc='center', 
        cellLoc='center', colLabels=list(df.columns)
    )
    table.set_fontsize(14)
    table.scale(3, 2.5)

    plt.show()
