arr=[1,3,4,5,6]
n=6
sum=0
n1=n*(n+1)/2

for i in range(len(arr)):
    sum=sum+arr[i]

print('Missing no ',int(n1-sum))
