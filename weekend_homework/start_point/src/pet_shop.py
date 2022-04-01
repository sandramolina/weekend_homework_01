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

def get_stock_count(pet_shop_list):
    return len(pet_shop_list["pets"])

def get_pets_by_breed(pet_shop_list, breed):
    breed_count = []
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == breed:
            breed_count.append(pet["name"])
    
    return breed_count

def find_pet_by_name(pet_shop_list, pet_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop_list, pet_name):
    selected_pet = find_pet_by_name(pet_shop_list, pet_name)
    pet_shop_list["pets"].remove(selected_pet)

def add_pet_to_stock(pet_shop_list, new_pet_obj):
    pet_shop_list["pets"].append(new_pet_obj)

def get_customer_cash(customer_list):
    return customer_list["cash"]