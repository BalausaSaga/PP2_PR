# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

Dog().speak()

# 2
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Bike(Vehicle):
    def move(self):
        print("Bike rides")

Bike().move()

# 3
class Person:
    def info(self):
        print("Person info")

class Teacher(Person):
    def info(self):
        print("Teacher info")

Teacher().info()

# 4
class Shape:
    def area(self):
        print("Shape area")

class Circle(Shape):
    def area(self):
        print("Circle area")

Circle().area()

# 5
class Parent:
    def hello(self):
        print("Parent hello")

class Child(Parent):
    def hello(self):
        print("Child hello")

Child().hello()