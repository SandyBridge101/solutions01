def swap_case(s):
    result=""
    for letter in s:
        if letter.islower()==True:
            result=result+letter.upper()
        else:
            result=result+letter.lower()
    return result

swap_case("Hello World")