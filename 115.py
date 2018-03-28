n=int(input("Enter the n value:"))
m=int(input("Enter the m value:"))
a=[]
for i in range(n):
	k=int(input())
	a.append(k)
for i in range(m-1):
        a.remove(min(a))
print(min(a))
