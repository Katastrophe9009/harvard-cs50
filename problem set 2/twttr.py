def main():
    user_input = (input("Input: "))
    print("Output: " + str(remove_vowels(user_input)))
def remove_vowels(user_input):
    result = ""
    for char in user_input:
        if char not in "aeiouAEIOU":
            result += char
    return result
main()