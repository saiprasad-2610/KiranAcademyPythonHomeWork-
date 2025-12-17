s1 = {10,"sai", 20,30}
s2 = {"kiran Academy",50,30,"sai","Pune"}
print("This is Set 1:",s1)
print("This is Set 2:",s2)
s1.add("New Element")
print("Add Element to Set 1:",s1 )
print("This is Intersection of Sets",s1.intersection(s2))  
print("This is Union of Sets",s1.union(s2))


print("-----------Remove the Duplicates from the List-------------")
l1 = [10,20,10,30,10,40,20,50]
print("Original List:",l1)
s = set(l1)
l2 = list(s)
print("Final Sorted List: ",l2)

set1={}
for value in l1:
    if value in set1:
        set1[value] +=1
    else:
        set1[value] =1 
for value in l2:
    print("delete",value,"=",set1[value]-1,"time")

print("---------Frozenset Example:-----------")
fs = frozenset([10,20,30,40,50])
print("This is Frozenset:",fs)
print("Type of fs is:",type(fs))