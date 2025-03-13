from application.console_gui import *
from application.user_input import *

def main() :
    while True :
        initial_action_choice = initial_action()

        if initial_action_choice == 1:
            collection_action = choose_collection_action()
            if collection_action == 1:
                create_product_action()
            else : 
                delete_product_action()
        elif initial_action_choice == 2:
            select_product_action()

main()