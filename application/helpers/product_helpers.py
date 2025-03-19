from application.operations import handle_read_operation
from .string_helpers import interpolate_attributes_to_string

def interpolate_product_string():
    product_data = handle_read_operation("productData.json")
    string: str = "\n "

    for key, product in product_data.items() :
        temp_string: str = f"[ {product["product_name"]} ]    |     "
        string = " ".join([string, temp_string])

    return string


def extract_product_attributes(product):
    attributes_array = []

    for attribute in product.keys():
        attributes_array.append(attribute)
    
    return attributes_array


def get_product_attributes(product_name):
    product_attribute_dictionary = define_product_attributes_dictionary(product_name)
    interpolated_attributes = interpolate_attributes_to_string(product_attribute_dictionary)

    return interpolated_attributes


def define_product_attributes_dictionary(product_name) -> dict:
    product_data = handle_read_operation("productData.json")
    product_attribute_array = extract_product_attributes(product_data[product_name])

    dictionary = {}

    for i in range(0, len(product_attribute_array)):
        dictionary[i+1] = product_attribute_array[i]
    
    return dictionary


def resolve_index_to_attribute(product_name: str, selected_index: int):
    product_attribute_dictionary = define_product_attributes_dictionary(product_name)
    value = product_attribute_dictionary[selected_index]

    return value