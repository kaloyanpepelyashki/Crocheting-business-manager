import json
from infrastructure.file_system import read_from_json, write_to_json

def handle_write_operation(file_path, key, value):
    try:
        data = read_from_json(file_path)
        
        if isinstance(data, dict):  
            data[key] = value  
        else:
            raise ValueError("⚠️ Error saving product")

        write_to_json(file_path, data)

    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")