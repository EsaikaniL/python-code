n=input("Enter the string:")
a=[]
flag=0
for i in n:
    if i not in a:
        a.append(i)
    else:
        flag=1
if(flag==1):
    print("no")
else:
    print("yes")
    
