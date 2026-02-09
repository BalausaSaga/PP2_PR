# 1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

Dog().speak()

# 2
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

Car().move()

# 3
class Person:
    def info(self):
        print("I am a person")

class Student(Person):
    pass

Student().info()

# 4
class Shape:
    def area(self):
        print("No area")

class Circle(Shape):
    pass

Circle().area()

# 5
class Parent:
    def hello(self):
        print("Hello from parent")

class Child(Parent):
    pass

Child().hello()