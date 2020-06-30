# A simple code to print the fibonacci sequence of a given number
# This code allows the user to input the fibonacci number they require

n = int(input("Enter the required number of series: "))

def Fibonacci(n):
    a = 0
    b = int(input("Enter required Fibonacci number: "))
    #c = a + b

    if n <= 0:
        print("Please enter a positive integer")
    elif n == b:
        print("Fibonacci sequence of ", n, ":")
        print(b)
    elif n>1:
        for i in range(0, n):
            c = a + b
            print(c)
            a,b = b,c
Fibonacci(n)