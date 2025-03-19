from unicodedata import numeric
from application.helpers.product_helpers import resolve_index_to_attribute
from infrastructure.cli import input_validator


def get_valid_product_name_input() -> str:
    while True:
        product_to_update = input_validator("Choose product to update > ")

        if not product_to_update :
            print("❌ Provide a product name!")
            continue 

        return product_to_update


def get_valid_attribute_name_input() -> int:
    while True:
        attribute_to_update = input_validator("Choose attribute to update > ")

        if not attribute_to_update :
           print("❌ Provide an attribute to update!")
        
        if not attribute_to_update.isnumeric() or not int(attribute_to_update) >= 1 and int(attribute_to_update) <= 5:
            print("❌ The selected value must be valid [1 - 5]")

        return int(attribute_to_update)


def get_valid_new_value_input(prompt: str, old_value):
    while True:
        new_value = input_validator(prompt)

        if not new_value:
            print("❌ Provide a new value!")

        match old_value:
            case int():
                if not new_value.isnumeric():
                     print("❌ The value must be numeric!")
                     continue
                return int(new_value)
            case float():
                try:
                    return float(new_value)
                except: 
                    print("❌ Problem registering value, try again!")
                    continue
            case str():
                return str(new_value)
            case _:
                print("❌ Invalid value")