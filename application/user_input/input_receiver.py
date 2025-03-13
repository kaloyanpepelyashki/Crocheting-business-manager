import math
import json
from application.console_gui import *
from models import *
from application.helpers import *
from .create_product_input_receiver import *
from infrastructure.file_system import *
from infrastructure.cli import *

def initial_action():
    clean_console()
    display_initial_action_banner()

    while True:
        try:
            selected_action = int(input_validator("Select action (1 or 2) > "))

            if selected_action != 1 and selected_action != 2:
                print("❌ Invalid choice. Please enter either 1 or 2.")
            else:
                return selected_action
        except ValueError:
            print("❌ Please enter a number (1 or 2).")

def select_product_action():
    clean_console()
    with open("productData.json", "r") as file:
        data = json.load(file)
        product_data = json.loads(json.dumps(data))


    display_banner()
    product_type_selected = input_validator("Product type > ")
    amount = int(input_validator("Amount > "))

    for key, product in product_data.items():
        if product["product_name"] == product_type_selected:
            product = Product(**product_data[key]) 
            price = product.calculate_price(amount)
            display_receipt(product, amount, price["total_price"], price["base_price"])

    input("🔵 Press Enter to continue...")
    return

def choose_collection_action() :
    clean_console()
    display_collection_action_banner()

    while True:
        collection_action = int(input_validator("Choose an action > "))
        if collection_action == 1 or collection_action == 2 or collection_action == 3:
            return collection_action
        else:
            print("Please select a valid option 1 - 3")
    
def create_product_action() :
    clean_console()
    display_create_product_banner()
    product_name = get_product_name()
    needed_yarn_grams = get_needed_yarn()
    needed_eyes = get_needed_eyes()
    needed_time_minutes = get_time_needed()
    difficulty_rate_percent = get_difficulty_level()

    append_to_json(product_name, {"needed_yarn_grams": needed_yarn_grams, "needed_time_minutes": needed_time_minutes, "needed_eyes": needed_eyes, "difficulty_rate_percent": difficulty_rate_percent, "product_name": product_name })
    display_new_product_receipt(product_name, needed_yarn_grams, needed_eyes, needed_time_minutes, difficulty_rate_percent)
    input("🔵 Press Enter to continue...")

def delete_product_action() :
    clean_console()
    display_delete_product_banner()

    while True:
        product_to_delete = input_validator("Type in the product name > ")

        if len(product_to_delete) > 0:
            clean_console()
            display_deletion_confirmation()
            deletion_confirmation = input_validator("Choose an action > ")

            if deletion_confirmation == "yes" or deletion_confirmation == "y":
                delete_from_json(product_to_delete)
                input("🔵 Press Enter to continue...")
                return
            else: 
                return
        else :
            print("❌ Type a valid product name")

