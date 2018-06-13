####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Nosferatu Zodd"
signature_flavors = "Berserker"
order_list = []


def print_menu():
    """
   Print the items in the menu dictionary.
    """
print("Our menu consists of these items (all amounts in KD):")
for key in menu:
    print key, menu[key]

def print_originals():
    """
    Print the original flavor cupcakes.
    """
print("Our original flavor cupcakes (KD %s each):" % original_price)
    

for index, item in enumerate(original_flavors):
    print index+1, item

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
print("Our signature flavor cupcake (KD %s each):" % signature_price)

print(signature_flavors)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return True

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []



    order = input("What is your your order? Please enter the correct spelling Type 'Exit' to end your order.)\n")
    while order.lower() != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()
    
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        order = order.lower()
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price
    
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("You ordered: ")
    for order in order_list:
        print("- %s " % order)

    print()
    price = get_total_price(order_list)
    print("That'll be KD %s" % price)
    if accept_credit_card(price):
        print("This order is eligible for credit card payment.")
