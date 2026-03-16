# 1. Using zip to pair two lists
names = ["Balausa", "Madina", "Sezim"]
scores = [95, 88, 92]

# 2. Using enumerate to add a counter
# enumerate(zip(...), 1) starts counting from 1
print("Student List:")
for i, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{i}. {name} got {score} points")

# 3. Type checking
val = "17"
if isinstance(val, str):
    num = int(val)
    print(f"\nConverted {type(val)} to {type(num)}")