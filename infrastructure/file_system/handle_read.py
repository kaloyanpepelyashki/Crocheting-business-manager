import json

def read_from_json(file_path) :
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            product_data = json.loads(json.dumps(data))

        return product_data
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error reading file")