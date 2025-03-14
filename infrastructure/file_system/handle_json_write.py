import json

def write_to_json(file_path, data_to_write):
    try:
        with open(file_path, "w") as file:
            json.dump(data_to_write, file, indent=4)

    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")
