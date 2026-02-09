# Example 1
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))

# Example 2
nums = [10, 20, 30, 40]
print(list(filter(lambda x: x > 25, nums)))

# Example 3
words = ["dog", "cat", "elephant"]
print(list(filter(lambda w: len(w) > 3, words)))

# Example 4
nums = [-5, -2, 0, 3, 8]
print(list(filter(lambda x: x >= 0, nums)))

# Example 5
nums = [1, 11, 21, 31]
print(list(filter(lambda x: str(x).startswith("1"), nums)))