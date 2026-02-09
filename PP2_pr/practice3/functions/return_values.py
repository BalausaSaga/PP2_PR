# 1. 
def string_length(s):
    return len(s)

print(string_length("Python"))

# 2. 
def squares(n):
    return [i**2 for i in range(1, n+1)]

print(squares(5))

# 3. 
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(10, 7))

# 4. 
def is_positive(x):
    return x > 0

print(is_positive(-3))

# 5.
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4]))