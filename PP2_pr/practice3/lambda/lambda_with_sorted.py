# Example 1
nums = [5, 2, 9, 1]
print(sorted(nums, key=lambda x: x))

# Example 2
words = ["apple", "banana", "cherry"]
print(sorted(words, key=lambda w: len(w)))

# Example 3
pairs = [(1, 3), (2, 2), (3, 1)]
print(sorted(pairs, key=lambda p: p[1]))

# Example 4
words = ["dog", "cat", "elephant"]
print(sorted(words, key=lambda w: w[-1]))

# Example 5
nums = [10, -5, 3, -2]
print(sorted(nums, key=lambda x: abs(x)))