def mergeAlternately(word1: str, word2: str) -> str:
    result=""
    size=len(word1) if len(word1) > len(word2) else len(word2)
    print(size)
    for x in range(0,size):
        if x>len(word1)-1:
            result=result+word2[x]
        elif x>len(word2)-1:
            result=result+word1[x]
        else:
            result=result+word1[x]+word2[x]

    return result

print(mergeAlternately("ab","pqrs"))