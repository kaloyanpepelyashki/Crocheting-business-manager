from application.helpers import interpolate_product_string

def display_initial_action_banner(): 
    print("\n" + "=" * 60)
    print(" " * 18 + "🧶 CROCHET BUSINESS APP 🧶")
    print("=" * 60)
    
    print("\n📌 What would you like to do?")
    print("\n➕  [ 1 ] Edit Collection")
    print("🧵  [ 2 ] Create a product (fulfill an order)")
    print("\n  [ exit ] or [ ex ] to exit the program")

    print("\n" + "-" * 60)

def display_collection_action_banner():
    print("\n" + "=" * 60)
    print("📦   PRODUCT COLLECTION MANAGEMENT   📦".center(60))
    print("=" * 60)
    print("")
    print("🔹 [ 1 ]  Add a New Product")
    print("🔹 [ 2 ]  Delete an Existing Product")
    print("🔹 [ 3 ]  Edit a Product")
    print("")
    print("\n [ exit ] or [ ex ] to exit the program")
    print("=" * 60 + "\n")

def display_create_product_banner():
    print("\n" + "=" * 60)
    print(" " * 16 + "🧶 LET'S ADD YOUR PRODUCT! 🧶")
    print("=" * 60)
    print("\n📌 Follow the steps below to add your product to the collection!\n")

def display_delete_product_banner():
    product_names_string = interpolate_product_string()
    print("\n" + "=" * 40)
    print("🗑️  DELETE A PRODUCT".center(40))
    print("=" * 40)
    print("Products: ")
    print(product_names_string)
    print("\n" + "=" * 50 + "\n")
    print("⚠️ Note: This action is irreversible!")

def display_deletion_confirmation():
    print("\n" + "=" * 30)
    print("⚠️  CONFIRM DELETION  ⚠️".center(30))
    print("=" * 30)
    print("")
    print("❗ Are you sure you want to delete this product?")
    print("   This action cannot be undone.")
    print("")
    print("✔️  Type [ yes ] or [ y ] to confirm.")
    print("❌  Type [ no ] or [ n ] to cancel.")
    print("=" * 30 + "\n")

def display_update_product_banner() :
    product_names_string = interpolate_product_string()
    print("\n" + "=" * 50)
    print("📦   UPDATE PRODUCT DETAILS   ✏️")
    print("=" * 50)
    print("")
    print("🔄 Modify an existing product in your collection.")
    print("You can update the name, materials needed, or other details.")
    print("")
    print("Products: ")
    print(product_names_string)
    print("")
    print("🔹 Follow the prompts to make changes.")
    print("")
    print("=" * 50 + "\n")