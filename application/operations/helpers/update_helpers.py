def validate_product_exists(data_set, product_key) -> bool :
    product_data = data_set

    if not product_data[product_key]:
        return False
    else: 
        return True

def validate_attribute_exists(product, attribute):
    if not product[attribute]:
        print("Attribute does not exist on product")
        return False
    else :
        return True
