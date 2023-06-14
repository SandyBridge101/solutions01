n = int(input())
nums = list(map(int, input().split()))
nums.sort()

negative = [i for i in nums if i<0]
positive = [i for i in nums if i>0]
zero = [i for i in nums if i==0]

if len(positive)==0:
    if len(negative)%2==0:
        positive.append(negative.pop())
        positive.append(negative.pop())
        zero.append(negative.pop())
    else:
        positive.append(negative.pop())
        positive.append(negative.pop())


if len(negative)%2==0:
    zero.append(negative.pop())




print(len(negative),*negative)
print(len(positive),*positive)
print(len(zero),*zero)

