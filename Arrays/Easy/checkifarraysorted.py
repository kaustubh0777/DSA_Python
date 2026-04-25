arr=[1,2,3,4,5]
flag=-1

for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        flag=1
        break

if(flag==1):
    print('Not sorted')
else:
    print('Sorted')

