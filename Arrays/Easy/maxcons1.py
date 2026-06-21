arr = [1, 0, 1, 1, 0, 1]
c=0
maxc=0

i=0

while i<len(arr):
    if arr[i]==1:
        c+=1
    else:
        maxc=max(maxc,c)
        c=0
    i+=1

if(c!=0):
    maxc=max(maxc,c)


print('Max consecutive one', maxc)