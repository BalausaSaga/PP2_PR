#1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = 5
for sq in square_generator(n):
    print(sq)

#2
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = 5
for sq in square_generator(n):
    print(sq)

#3
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)

n = int(input("Enter n: "))
print(", ".join(even_generator(n)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for val in squares(3, 7):
    print(val)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for x in countdown(5):
    print(x)