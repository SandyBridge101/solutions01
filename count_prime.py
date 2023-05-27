def countPrimes( n: int) -> int:
    count=0
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            count=count+1
    return count
    
    
print(countPrimes(499979))
#print(elimination(3,elimination(2,[1,2,3,4,5,6,7,8,9,10],10),10))