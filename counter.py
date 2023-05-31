from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
#print(Counter(myList).keys())
#2 3 4 5 6 8 7 6 5 18
N=int(input())
X=int(input())
i=0
profit=0
shoe_sizes=input("sizes:").split()

while i<X:
    order=input("order:").split()
    if order[0] in shoe_sizes:
        #print("In list")
        profit=profit+int(order[1])
        shoe_sizes.remove(order[0])
        #print(f'Profit:{profit}')

    i+=1

print(profit)


print(shoe_sizes)

