# WRITE YOUR FUNCTIONS HERE 23 total

def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash_in_out):
    list["admin"]["total_cash"] += cash_in_out

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

def increase_pets_sold(list, new_pet_sold):
    list["admin"]["pets_sold"] += new_pet_sold