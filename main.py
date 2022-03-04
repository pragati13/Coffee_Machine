MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
flag = True
water_1 = resources["water"]
milk_1 = resources["milk"]
coffee_1 = resources["coffee"]


def money_format():
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    t = 0.25*q + 0.10*d + 0.05*n + 0.01*p
    return t


def pending_resources(parameter):
    global water_1, milk_1, coffee_1
    if parameter == "latte" or parameter == "cappuccino":
        water_1 = water_1 - MENU[parameter]["ingredients"]["water"]
        milk_1 = milk_1 - MENU[parameter]["ingredients"]["milk"]
        coffee_1 = coffee_1 - MENU[parameter]["ingredients"]["coffee"]
    elif parameter == "espresso":
        water_1 = water_1 - MENU[parameter]["ingredients"]["water"]
        coffee_1 = coffee_1 - MENU[parameter]["ingredients"]["coffee"]


def coffee_check(param):
    global money
    if MENU[param]["ingredients"]["water"] > water_1:
        print("Sorry there is not enough water.")
    elif MENU[param]["ingredients"]["coffee"] > coffee_1:
        print("Sorry there is not enough coffee.")
    elif param != "espresso" and MENU[param]["ingredients"]["milk"] > milk_1:
        print("Sorry there is not enough milk.")
    elif MENU[param]["ingredients"]["water"] < water_1 and MENU["espresso"]["ingredients"]["coffee"] < coffee_1:
        total = money_format()
        if total >= MENU[param]["cost"]:
            money = money + MENU[param]["cost"]
            pending_resources(param)
            remaining_change = total - MENU[param]["cost"]
            print(f"Here is ${round(remaining_change,2)} in change.")
            print(f"Here is your {param} ☕. Enjoy!")
        elif total < MENU[param]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
    coffee_machine()


def coffee_machine():
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == "report":
        print(f"Water : {water_1}")
        print(f"Milk : {milk_1}")
        print(f"Coffee : {coffee_1}")
        print(f"Money : ${money}")
        coffee_machine()
    elif coffee_type == "off":
        exit(0)
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        coffee_check(coffee_type)


coffee_machine()

# latte : 2.5 - 10q , capuccino : 3 - 12q , espresso : 1.5 - 6q
