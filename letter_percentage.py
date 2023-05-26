def percentageLetter(s: str, letter: str) -> int:
    count=0
    for character in s:
        if character==letter:
            count=count+1
    percentage=int((count/len(s))*100)
    return percentage
    
print(percentageLetter("passsword","s"))