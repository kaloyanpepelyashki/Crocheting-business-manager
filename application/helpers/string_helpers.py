from application.operations import handle_read_operation

def interpolate_product_string():
    product_data = handle_read_operation("productData.json")
    string: str = "\n "

    for key, product in product_data.items():
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string