def Upper_Row(a,n):
    if n == 1:
        return 
    else:
        print("* "*n+" "*(4*a-4*n)+"* "*n) 
        return Upper_Row(a,n-1)

def Lower_Row(a,n):
    if n == 0:
        return
        
    else:
        Lower_Row(a,n-1)
        print("* "*n+" "*(4*a-4*n)+"* "*n)

n = int(input("Enter the value of n:"))
Upper_Row(n,n)
Lower_Row(n,n)