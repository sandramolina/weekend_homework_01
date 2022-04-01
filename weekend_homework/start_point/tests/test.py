customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

def find_pet_by_name(pet_shop_list, pet_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop_list, pet_name):
    selected_pet = find_pet_by_name(pet_shop_list, pet_name)
    pet_shop_list["pets"].remove(selected_pet)

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def remove_customer_cash(customer, cash_to_rm):
    customer["cash"] -= cash_to_rm

def increase_pets_sold(pet_shop_list, new_pet_sold):
    pet_shop_list["admin"]["pets_sold"] += new_pet_sold

def add_or_remove_cash(pet_shop_list, cash_in_out):
    pet_shop_list["admin"]["total_cash"] += cash_in_out

def sell_pet_to_customer(pet_shop_list, pet_name, customer):
    pet_to_be_sold = find_pet_by_name(pet_shop_list, pet_name)
    pet_price = pet_to_be_sold["price"]
    if customer["cash"] >= pet_price:
        remove_pet_by_name(pet_shop_list, pet_name)
        add_pet_to_customer(customer, pet_to_be_sold)
        increase_pets_sold(pet_shop_list, 1)
        remove_customer_cash(customer, pet_price)
        add_or_remove_cash(pet_shop_list, pet_price)

customer1 = customers[0]
sell_pet_to_customer(cc_pet_shop, "Arthur", customer1)
print(len(customer1["pets"]))
print(cc_pet_shop["admin"]["pets_sold"])