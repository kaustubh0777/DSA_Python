n = int(input("Enter a no "))
i=n
rev=0
while(i!=0):
    d=i%10
    rev=rev*10+d
    i=i//10

if(rev==n):
    print("Yes")
else:
    print("No")