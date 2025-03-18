from application.operations import handle_read_operation

def interpolate_product_string() :
    product_data = handle_read_operation("productData.json")
    string: str = "\n "

    for key, product in product_data.items() :
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string

def interpolate_attributes_to_string(attributes_array): 
    string = ""

    for i in range(0, len(attributes_array)):
        temp_string = f"[ {i + 1} ]. {attributes_array[i]}"
        string = " ".join([string, temp_string])
    
    return string
