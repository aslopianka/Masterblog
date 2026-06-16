import json


def load_data_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)