# 1 simple / single
# class Parent:
#     def f1(self):
#         print("I am parent..")
# class Child(Parent):
#     def f2(self):
#         print("i am child...")
# c1 = Child()
# c1.f1()
# c1.f2()

# 2 multi - level
# class grandParents:
#     def p1(self):
#         print("this is Grand parent")
# class Parents(grandParents):
#     def p2(self):
#         print("This is Parents")
# class Childs(Parents):
#     def p3(self):
#         print("This is child ")
# c1 = Childs()
# c1.p1()
# c1.p2()
# c1.p3()


# #3 multiple ----- child class inherit multiple parent class
# class father():
#     def f1(self):
#         print("this is father")
# class mother():
#     def m1(self):
#         print("This is mother")
# class child(father,mother):
#     def c1(self):
#         print("this is child")
# c1 = child()
# c1.f1()
# c1.m1()
# c1.c1()

#4 Herircial ---- multiple child class inherit single parent class
# class parent():
#     def p1(self):
#         print("This is Parent")
# class child1(parent):
#     def c1(self):
#         print("This is child 1")
#         self.p1()
# class child2(parent):
#     def c2(self):
#         print("this is child2")
# c1 = child1()
# c1.c1()

#5 Hybrid -- two or more inheritance types are combined


#6 Cyclic -- In python the cyclic type is not allowed 

class parent:
    def __init__(self):
        print("This is parenet consructor")
class child(parent):
    def __init__(self):
        print("THis is child constrcutor")
c1 = child()
c1.__init__()