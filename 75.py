str=input("Enter the string:")
l=len(str)
str1=list(str)
k=round(l//2)
str1[k]='*'
out=''
for i in str1: 
        out=out+i 
print(out)
