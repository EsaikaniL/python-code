def hasvowel():
       v=['a','e','i','o','u','A','E','I','O','U']
       str=input("Enter the string:")
       for i in str:
            if i in v:
                print("yes")
                break;
	
try:
    hasvowel();
except:
    print("invalid")
