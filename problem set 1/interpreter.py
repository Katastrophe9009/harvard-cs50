def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    if y == "+":
        print(float(int(x) + int(z)))
    elif y == "-":
        print(float(int(x) - int(z)))
    elif y == "*":
        print(float(int(x) * int(z)))
    elif y == "/" and int(z) != 0:
        print(float(int(x) / int(z)))
    else:
        print("Please enter a valid expression...")
main()