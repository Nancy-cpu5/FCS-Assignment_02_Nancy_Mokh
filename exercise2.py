#Exercise 2

def Divisors():
    n=int(input('Enter a positive integer'))
    i=1
    Divisorr=[]
    while (i<=n):
        if n%i==0 :
         Divisorr.append(i)
        i+=1
    return Divisorr
The_Divisors=Divisors()
print(f" the divisors are {The_Divisors}")

