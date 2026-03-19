def main():
    greeting = input("Greeting: ").casefold().strip()
    if greeting.startswith("hello", 0):
        print("$0")
    elif greeting.startswith("h", 0):
        print("$20")
    else:
        print("$100")

main()