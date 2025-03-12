import json

def append_to_json(key, value):
    FILE_PATH = "productData.json"
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file) 
        
        if isinstance(data, dict):  
            data[key] = value  
        else:
            raise ValueError("⚠️ Error saving product")

        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Problem saving product")
