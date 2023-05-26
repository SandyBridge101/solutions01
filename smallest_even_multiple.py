def smallestEvenMultiple( n: int) -> int:
    x=1
    while True:
        multiple=n*x
        if (multiple)%2==0:
            return multiple
        x=x+1
print(smallestEvenMultiple(5))