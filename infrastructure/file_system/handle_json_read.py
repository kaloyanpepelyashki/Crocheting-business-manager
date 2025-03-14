import json

def read_from_json(file_path) :
    try:
        with open(file_path, "r") as file:
            file.seek(0)
            data = json.load(file)
            return data

    except (json.JSONDecodeError, FileNotFoundError):
        print("Error reading file")