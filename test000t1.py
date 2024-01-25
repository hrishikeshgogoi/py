#Polymorphism and Inheritance
class Base():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def lee(self):
        print(f"{self.a} is a {self.b}")
    def goo(self):
        print(f"{self.c} like playing {self.d}")
class Polymorph(Base):
    def __init__(self,a,b,c,d,e):
        super().__init__(a,b,c,d)
        self.e=e
    def lee(self):
        print(f"{self.d} is a {self.e}")
class Poly():
    def goo(self):
        print("Jake also likes to play table tennis")
x=Base("Jake","student","He","guitar")
y=Polymorph("","","","Guitar","musical instrument")
z=Poly()
x.lee()
x.goo()
y.lee()
z.goo()