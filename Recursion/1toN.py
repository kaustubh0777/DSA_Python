def solve(n):
    if(n<1):
        return 
    else:
        solve(n-1)
        print(n)

n=int(input('Enter no \n'))
solve(n)