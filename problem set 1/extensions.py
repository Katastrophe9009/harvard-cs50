def main():
    file = input("File name: ").casefold().strip().split(".")
    print(file)
    match file:
        case "gif":
            print("image/gif")



main()