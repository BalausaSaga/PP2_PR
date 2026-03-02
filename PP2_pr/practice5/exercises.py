import re

# 1. 'a' followed by zero or more 'b's
def task1(text):
    return re.fullmatch(r"ab*", text) is not None

# 2. 'a' followed by two to three 'b's
def task2(text):
    return re.fullmatch(r"ab{2,3}", text) is not None

# 3. Lowercase letters joined with an underscore
def task3(text):
    return re.findall(r"[a-z]+_[a-z]+", text)

# 4. One upper case letter followed by lower case letters
def task4(text):
    return re.findall(r"[A-Z][a-z]+", text)

# 5. 'a' followed by anything, ending in 'b'
def task5(text):
    return re.fullmatch(r"a.*b", text) is not None

# 6. Replace space, comma, or dot with a colon
def task6(text):
    return re.sub(r"[ ,.]", ":", text)

# 7. Snake case to camel case
def task7(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# 8. Split at uppercase letters
def task8(text):
    return re.findall(r"[A-Z][^A-Z]*", text)

# 9. Insert spaces between words starting with capitals
def task9(text):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", text)

# 10. Camel case to snake case
def task10(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()