def sol(nam,n):
    if(n>=1):
        print(nam)
        sol(nam,n-1)
    else:
        return

nam=input('Enter your name \n')
n=int(input('How many times to print \n'))

sol(nam,n)