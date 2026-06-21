arr=[1,2,3,4,5]

x=int(input('Enter the no u want to search'))
f=0

for i in range(len(arr)):
    if(arr[i]==x):
        f=1
        print('Found')
        break

if f!=1:
    print('Not')