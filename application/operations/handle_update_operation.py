import json
from infrastructure.file_system import read_from_json, write_to_json
from .helpers import validate_product_exists, validate_attribute_exists

def handle_update_product_operation(file_path, product_key, attribure_to_update, new_value) -> bool:
    try:
        product_data = read_from_json(file_path)

        if not product_data:
            print("Error getting data")
            return False   
            
        product_valid = validate_product_exists(product_data, product_key)
        if not product_valid:
            print("Product does not exist")
            return False
        
        attribute_valid = validate_attribute_exists(product_data[product_key], attribure_to_update)
        if not attribute_valid:
            print(f"Attribure does not exist on {product_data[product_key]}")
            return False
    

        product_data[product_key][attribure_to_update] = new_value

        write_to_json(file_path, product_data)
    except (json.JSONDecodeError, FileNotFoundError):
        pass