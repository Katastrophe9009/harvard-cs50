def main():
    convert_to_snake(input("camelCase: "))
def convert_to_snake(input):
    for letter in input:
        if letter != letter.lower():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()
main()