import csv


def extract_data(path: str):
    """
    Take a path to a csv file as a str and return the content as a list.
    """
    container_list = []
    with open(path, "r") as data_file:
        csv_reader = csv.DictReader(data_file)
        for row in csv_reader:
            container_list.append(row)
    return container_list
