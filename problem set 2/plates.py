def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if check1(s) and check2(s) and check3(s) and check4(s):
        return True
    else:
        return False
def check1(s):
    #All vanity plates must start with at least two letters.
    if s[0:2].isalpha():
        return True
    return False
def check2(s):
    #Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if 2 <= len(s) <= 6:
        return True
    return False
def check3(s):
    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would
    # be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    found_number = False
    for char in s:
        if char.isdigit():
            if found_number == False:
                if char == "0":
                    return False
            found_number = True
        else:
            if found_number:
                return False    
    return True
def check4(s):
    #“No periods, spaces, or punctuation marks are allowed.”
    if s.isalnum():
        return True
    return False
main()
