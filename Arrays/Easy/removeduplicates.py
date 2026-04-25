def remdup(arr):
    r=1
    w=0
    n=len(arr)
    while(r<n):
        if arr[r]==arr[w]:
            r+=1
        elif arr[r]!=arr[w]:
            w+=1
            arr[w]=arr[r]
            r+=1
            
    
    for i in range(0,w):
        print(arr[i])



arr=[1,2,2,3,4,4,4,5]
remdup(arr)


