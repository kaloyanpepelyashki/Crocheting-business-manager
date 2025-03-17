import json
from infrastructure.file_system import read_from_json, write_to_json

def handle_write_new_product_operation(file_path, key, value) -> bool :
    try:
        data = read_from_json(file_path)
        
        if key in data :
            print("❌ Product with this name already exists")
            return False
        else :
            if isinstance(data, dict):  
                data[key] = value  
            else :
                raise ValueError("⚠️ Error saving product")

        write_to_json(file_path, data)
        return True

    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")
        return False