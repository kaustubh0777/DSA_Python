n=int(input('Enter a no \n'))

i=n
sum=0
while(i):
    d=i%10
    sum+=pow(d,3)
    i=i//10

if sum==n:
    print('The no is armstrong no')
else:
    print('NOT')
