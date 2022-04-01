# WRITE YOUR FUNCTIONS HERE 23 total

def get_pet_shop_name(pet_shop_list):
    return pet_shop_list["name"]

def get_total_cash(pet_shop_list):
    return pet_shop_list["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_list, cash_in_out):
    pet_shop_list["admin"]["total_cash"] += cash_in_out

def get_pets_sold(pet_shop_list):
    return pet_shop_list["admin"]["pets_sold"]

def increase_pets_sold(pet_shop_list, new_pet_sold):
    pet_shop_list["admin"]["pets_sold"] += new_pet_sold

# def get_stock_count():
