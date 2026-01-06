# #  Find all the pairs whose sum is equal to K in a list of integers
# listOfIntegers = [10, 15, 3, 7, 8, 5, 2, 12]
# k = int(input("Enter the K value: "))
# for i in range  (len(listOfIntegers)):
#     for j in range(len(listOfIntegers)):
#         if k == (listOfIntegers[i]+listOfIntegers[j]):
#             print(listOfIntegers[i], listOfIntegers[j])

# ls=[]
# for i in range(100,10,-1):
#     print(110-i)

# i = 1
# while(i<=10):
#     print(i)
#     i=1
# print(i)


# def rightAnglePattern(n):
#     for rows in range(1,n+1):
#          for cols in range(1,rows+1):
#              print("*", end=" ")
#          print()

# rightAnglePattern(5)

# def ReverserightAnglePattern(n):
#     for rows in range(n+1,1,-1):
#          for cols in range(rows+1,1,-1):
#              print("*", end=" ")
#          print()

# ReverserightAnglePattern(5)

# def rightAnglePattern1(n):
#     for rows in range(1,n+1):
#          for cols in range(1,rows+1):
#              print(chr(64+cols), end=" ")
#          print()
# rightAnglePattern1(5)

# pyramid
n=5
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)

# Reverse Pyramide
for i in range(n,0,-1):
    print(" "*(n-i),"* "*i)
    
def cal(x=5):
    return x+2;
print(cal(4))
