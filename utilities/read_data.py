import csv


def get_csv_data(file_name):
    """
    Get data from csv file
    :param file_name: Name of the file to read
    :return: list of data
    """
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
