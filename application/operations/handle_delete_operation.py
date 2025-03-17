import json
from infrastructure.file_system import read_from_json, write_to_json

def handle_delete_product_operation(file_path, key_to_delete) -> bool :
     try:
        data = read_from_json(file_path)

        if isinstance(data, dict) :
            if key_to_delete in data:
                del data[key_to_delete]
                print("Product deleted")
            else :
                print(f"❌ The name {key_to_delete} does not exist")
                return False
        else :
            raise ValueError("⚠️ Error deleting product")
        
        write_to_json(file_path, data)
        return True
    
     except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")

