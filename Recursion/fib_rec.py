__author__ = 'Aditya Pulekar'
def fib(n):
    if(n==0):
        return 0;
    elif(n==1):
        return 1;
    else:
        y=fib(n-1)+fib(n-2);
        return y;


def main():
    n=int(input("How many numbers do you want out of the fibonacci series?"))
    res=fib(n)
    #print("Press Enter to exit")
    print(res)

if __name__=='__main__':
    main()