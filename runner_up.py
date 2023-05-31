n = 5
arr = [57, 57, -57, 57]

mx=-100
ru=-100

for i in arr:
    if i>mx:
        ru=mx
        mx=i
        print(ru)
    elif ru<=i<mx:
        ru=i
        print(ru)
        
#print(ru)