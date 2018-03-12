n=int(input("Enter the integer1:"))
m=int(input("Entre the integer2:"))
a=[]
b=[]
c=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in range(1,m+1):
    if m%i==0:
        b.append(i)
for i in a:
    if i not in b:
        c.append(i)
print("LCM:",max(c))
