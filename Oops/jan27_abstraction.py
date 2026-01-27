from abc import ABC, abstractmethod


class Myclass(ABC):
    @abstractmethod
    def m2(self,a):
        pass
    def m1(self):
        print("Hello")
class child(Myclass):
    def m2(self,a):
            print(a+10)
c1 = child()
c1.m2(5)
c1.m1()