import math

def largest_non_perfect_square(arr):
    largest = float('-inf')
    for num in arr:
        sqrt_num = math.sqrt(num)
        if sqrt_num != int(sqrt_num):
            largest = max(largest, num)
    return largest

N=int(input())

array=list(map(int,input().split()))
result = largest_non_perfect_square(array)
print(result) 