n=int(input("Enter the n value:"))
m=int(input("Enter the m value:"))
a=[]
b=[]
for i in range(n):
	k=int(input())
	a.append(k)
for i in a:
	if i%2!=0:
		b.append(i)
print(b[m-1])
