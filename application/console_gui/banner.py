import json
from typing import List
from application.helpers import interpolate_product_string



def display_banner():
    product_names_string = interpolate_product_string()
    print("+" * 50)
    print("\n" + "=" * 50)
    print(" " * 15 + " CHOOSE A PRODUCT ")
    print("=" * 50)
    print("Products: ")
    print(product_names_string)
    print("\n" + "=" * 50 + "\n")
    print("+" * 50)
