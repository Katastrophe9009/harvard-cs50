menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main ():
    while True:
        item = get_item()
        add_to_total(item)

def get_item ():
    while True:
        try:
            item = (input("Item: ").title())
            if item in menu:
                return item
            else:
                pass
        except ValueError or EnvironmentError:
            pass

def add_to_total (item):
    global total
    total += menu[item]
    print(f"Total: ${total}")
total = 0 
main()