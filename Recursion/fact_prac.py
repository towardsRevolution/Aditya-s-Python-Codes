__author__ = 'Aditya Pulekar'

def fact_rec(n):
    if n<=1: #Having this base case is very efficient, bcoz then for n < 0, the max recursion depth ain't exceeded
        return 1
    # if n < 0:
    #     raise ValueError("Number is negative...")
    else:
        n=n*fact_rec(n-1)
    return n


def main():
    n=int(input("Enter the number whose factorial you want to calculate: "))
    res=fact_rec(n)
    print("Result: ",res)

main()