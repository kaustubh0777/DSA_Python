arr=[5,4,3,2,1]
min_idx=-1
for i in range(len(arr)):
    mini=100
    for j in range(i,len(arr)):
        if(arr[j]<mini):
            mini=arr[j]
            min_idx=j
    arr[min_idx],arr[i]=arr[i],arr[min_idx]


print(arr)

    
