slar=-1
lar=-1
arr=[1,2,3,4,5,6]

for i in range(len(arr)):
    if(arr[i]>lar and slar<arr[i]):
        slar=lar
        lar=arr[i]
    elif(arr[i]>slar and arr[i]<=lar):
        slar=arr[i]


print('Largest number',lar)
print('Second Largest',slar)
