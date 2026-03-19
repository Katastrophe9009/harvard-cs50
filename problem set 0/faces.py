def convert(input):
    smileys = str(input).replace(":)","🙂")
    converted = smileys.replace(":(","🙁")
    print(converted)

convert(input("Hi! "))