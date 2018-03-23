s=input("Enter a string and N value:")
str1=s.split(" ")[0][::-1]
n=int(s.split(" ")[1])
ans=''
for i in range(n):
	ans=ans+str1[i]
print(ans)
