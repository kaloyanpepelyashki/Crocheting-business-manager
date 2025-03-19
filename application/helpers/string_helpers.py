from application.operations import handle_read_operation

def interpolate_product_string() :
    product_data = handle_read_operation("productData.json")
    string: str = "\n "

    for key, product in product_data.items() :
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string

def normalize_attribute_string(s):
    return ' '.join(word.capitalize() for word in s.split('_'))

def interpolate_attributes_to_string(attributes_dict: dict) -> str:  
    interpolated_string = []
    
    for key, value in attributes_dict.items():
        attribute_name = normalize_attribute_string(value)
        interpolated_string.append(f"[ {key} ] {attribute_name}")

    return " | ".join(interpolated_string)