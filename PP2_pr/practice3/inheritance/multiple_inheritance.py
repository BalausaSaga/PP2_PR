# 1
class A:
    def action(self):
        print("Action from A")

class B:
    def action(self):
        print("Action from B")

class C(A, B):
    pass

C().action()

# 2
class X:
    def show(self):
        print("Show from X")

class Y:
    def show(self):
        print("Show from Y")

class Z(X, Y):
    pass

Z().show()

# 3
class Parent1:
    def hello(self):
        print("Hello from Parent1")

class Parent2:
    def hello(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    pass

Child().hello()

# 4
class Base1:
    def info(self):
        print("Info from Base1")

class Base2:
    def info(self):
        print("Info from Base2")

class Derived(Base1, Base2):
    pass

Derived().info()

# 5
class M:
    def test(self):
        print("Test from M")

class N:
    def test(self):
        print("Test from N")

class O(M, N):
    pass

O().test()