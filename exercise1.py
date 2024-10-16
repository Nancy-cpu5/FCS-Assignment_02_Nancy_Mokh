def factorial(n):
    i=1
    The_factorial=1
    while (i<=n):
        The_factorial*=i
        i+=1
    return The_factorial
n=int(input('Write a positive number'))
print (f"The factorial of {n} is {factorial(n)}")
