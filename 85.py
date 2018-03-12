n=input("Enter the string:")
even=""
odd=""
l=len(n)
for i in range(1,l+1):
    if(i%2==0):
        even=even+n[i-1]
    else:
        odd=odd+n[i-1]
print(odd,"",even)
