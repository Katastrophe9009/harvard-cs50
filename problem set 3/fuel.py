def main():
    while True:
        fraction = input("Fraction: ")
        percent = percentage(fraction)
        if percent is None or int(percent) < 0:
            pass
        elif int(percent) <= 1:
            return print("E")
        elif int(percent) >= 99:
            return print("F")
        else:
            return print(f"{percent}%")
def percentage(fraction):
    x, y = fraction.split(sep="/")
    try:
        x = int(x)
        y = int(y)
        if x == y:
            return int(100)
        elif x < y and y != 0:
            return int((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        pass
main()