# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

Dog().speak()

# 2
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        super().move()
        print("Car drives")

Car().move()

# 3
class Person:
    def info(self):
        print("Person info")

class Student(Person):
    def info(self):
        super().info()
        print("Student info")

Student().info()

# 4
class Shape:
    def area(self):
        print("Shape area")

class Square(Shape):
    def area(self):
        super().area()
        print("Square area")

Square().area()

# 5
class Parent:
    def hello(self):
        print("Parent hello")

class Child(Parent):
    def hello(self):
        super().hello()
        print("Child hello")

Child().hello()