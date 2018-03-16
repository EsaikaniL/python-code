n=int(input("Enter the n value:"))
a=[]
for i in range(n):
    s=int(input())
    a.append(s)
for i in range(n-1):
    for j in range(i,n):
        if(a[i]>a[j]):
            ans=i+1
print(ans)

        

    
    

