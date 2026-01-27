# # List Comprehension : -- creating a new list from another collection data type(set,list,range,tuple,dict)
# # Syntax >>>  new_list = [var for var in old_collection]

ls = [10,20,44,30,40,50]

# # new_list = [x for x in ls]
# print(ls)
# square_list = [x**2 for x in ls]
# print(square_list)

# cube from 20 to 30 and which are divisiable by 5 
cubeList =[x**3 for x in range(20,31) if x%5==0]
# print(cubeList)



# Dict Comprehension: -  creating a new Dict from another collection data type(set,list,range,tuple,dict)
# # Syntax >>>  new_Dict = [key:value for var in old_collection]

squareDict = {x:x**2 for x in ls}
# print(squareDict)

l = [(1,2),(3,4),(5,6)]
squared_list = [i**2 for x in l for i in x  ]
print(squared_list)

namels = [["sai","rahul"],["rohit","sham"]]
newName = [x.upper() for i in namels for x in i ]
print(newName)
ls.sort()
print(ls)