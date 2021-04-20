import csv


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        data = csv.DictReader(csvfile, fieldnames=["nome", "prato", "dia"])
        print(data)
