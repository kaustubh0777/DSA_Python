arr=dict()
res=[1,2,3,4,4,5]

for i in range(len(res)):
    # if no is already present
    if res[i] in arr:
        arr[res[i]]+=1
    else:
        arr[res[i]]=1


print(arr)