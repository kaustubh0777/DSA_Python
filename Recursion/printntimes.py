def solve(n):
    if(n>=0):
        print(n)
        n-=1
        solve(n)
    else:
        return
    
n=int(input('Enter a name'))
solve(n)
