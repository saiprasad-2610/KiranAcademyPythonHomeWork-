# temp =1
def fact(n):
    temp =1
    for i in range(1,n+1):
        temp = temp*i
    print(temp)
fact(int(input("Enter the number:")))

def sumOfNo(n):
    return (n*(n+1))/2
print(sumOfNo(5))

def fact1(n):
    if n==1:
        return 1
    else:
        return n * fact1(n-1)
print(fact1(5))

