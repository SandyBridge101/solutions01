from collections import OrderedDict

shop_list={}

#shop_list['banana']=[50.00,2]

#shop_list['banana']=[60.00,3]

print(shop_list)

N=9
i=0

while i<N:
    order=input("order:").split()
    print(order)
    for x in range(0,len(order)-1):
        if x==0:
            item=order[x]
        else:
            item=item+' '+order[x]
    price=order[len(order)-1]

    if item in shop_list.keys():
        shop_list[item]=int(shop_list[item])+int(price)
    else:
        shop_list[item]=int(price)
    i+=1
    
for key, value in shop_list.items():
    print(key, value)

