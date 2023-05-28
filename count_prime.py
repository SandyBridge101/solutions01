class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0

        sieve = [True] * n  
        sieve[0:n:2] = [False] * len(sieve[0:n:2])
        sieve[1], sieve[2] = False, True

        for i in range(3, int(n**0.5)+1, 2):
            if sieve[i] == True:
                sieve[i*i:n:i<<1] = [False] * len(sieve[i*i:n:i<<1])

        return sieve.count(True)
"""
    count=0
    numbers=[i for i in range(1, n)]
    if n<=1:
        return 0
    for x in range(2,n):
        if isprime(x)==True:
            if x*x<=n:
                elimination(x,numbers,n)
            
    return len(numbers)-1

"""