import json


def load_data_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_data_to_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)