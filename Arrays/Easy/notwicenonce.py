arr=[2,2,5]

res=arr[0]
ans=-1

arr=sorted(arr)

for i in range(1,len(arr)):
    if arr[i-1]^arr[i]==0:
        ans=arr[i-1]
    res=res^arr[i]



print('Single no',res)
print('Twice no',ans)