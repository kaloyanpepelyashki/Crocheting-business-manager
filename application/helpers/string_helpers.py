from infrastructure.file_system import read_from_json

def interpolate_product_string():
    product_data = read_from_json("productData.json")
    string: str = "\n "

    for key, product in product_data.items():
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string