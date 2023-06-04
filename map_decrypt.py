
s = "10#11#12"
for i in range(26,0,-1):
    s=s.replace(str(i)+"#",chr(ord('a')+i-1))if i>9 else s.replace(str(i),chr(ord('a')+i-1))
print(s)