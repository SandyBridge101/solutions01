def swap_case(s):
    result=""
    for letter in s:
        if letter.islower()==True:
            result=result+letter.upper()
            print(letter)
        else:
            result=result+letter.lower()
            print(letter)
    print(result)
    return

swap_case("Hello World")