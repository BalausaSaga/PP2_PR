#1
class MyClass:
  x = 5

print(MyClass)

#2
class MyClass:
  x = 50
print(MyClass)

#3
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#4
class Person:
  pass  #having an empty class definition like this, would raise an error without the pass statement
