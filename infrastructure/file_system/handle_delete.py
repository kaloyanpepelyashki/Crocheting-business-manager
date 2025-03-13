import json

def delete_from_json(key_to_delete) :
     FILE_PATH = "productData.json"
     try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
        
        if isinstance(data, dict) :
            if key_to_delete in data:
                del data[key_to_delete]
                print("Product deleted")
            else :
                print(f"❌ The name {key_to_delete} does not exist")
        else :
            raise ValueError("⚠️ Error deleting product")
        
        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)
    
     except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")

