import json
from typing import List

with open("productData.json", "r") as file:
    data = json.load(file)
    product_data = json.loads(json.dumps(data))

def interpolate_product_types():
    string: str = "\n "

    for key, product in product_data.items():
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string

product_names_string = interpolate_product_types()

def display_banner():
    print("+" * 50)
    print("\n" + "=" * 50)
    print(" " * 15 + " CHOOSE A PRODUCT ")
    print("=" * 50)
    print(product_names_string)
    print("\n" + "=" * 50 + "\n")
    print("+" * 50)
