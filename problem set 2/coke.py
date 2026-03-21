def main():
    price = 50
    while price > 0:
        print("Amount Due: " + str(price))
        coin = int(input("Insert Coin: "))
        if coin == 25:
            price -= 25
        elif coin == 10:
            price -= 10
        elif coin == 5:
            price -= 5
    print("Change Owed: " + str(price).strip("-"))
main()