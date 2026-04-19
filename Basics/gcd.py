
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    

    return gcd(b,a%b)



a=int(input('Enter the value of a \n'))
b=int(input('Enter the value of b \n'))

print('GCD of two nos is ',gcd(a,b))

