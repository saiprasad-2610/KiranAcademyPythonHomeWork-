# def addthree(x,y,z):
#     return(x+y+z)
# result = addthree(int(input("Enter 1st No: ")),int(input("Enter 2nd No: ")),int(input("Enter 3rd No: ")))
# print(f"Addition is {result}")

def addthree(x,y,z):
    sum = x+y+z
    return sum
def avgthree(sum):
    avg = sum/3
    return avg
average = avgthree(addthree(10,20,30))
def discount(avg):
    dis = (avg/100)*5
    return dis
disResult = discount(avgthree(addthree(10,20,30)))
# print(disResult)