n=int(input("Enter the n value:"))
out=0
while(n!=0):
	temp=n%10
	out=out*10+temp
	n=n//10
print(out)
