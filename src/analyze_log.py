import csv

def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as csv_file:
            return csv_file
    except FileExistsError:
        return 'File not found'
