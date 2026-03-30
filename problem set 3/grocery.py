def main():
    while True:
        try:
            item = input().upper()
            add_item(item)
        except KeyError:
            print("Invalid input")
        except EOFError:
            show_list(grocery_list)

def add_item(item):
    if item in grocery_list:
        grocery_list[item] += 1
        return grocery_list
    else:
        grocery_list[item] = 1
        return grocery_list

def show_list(grocery_list):
    sorted_list = sorted(grocery_list)
    for item in sorted_list:
        print(grocery_list[item], item)

grocery_list = {}
main()