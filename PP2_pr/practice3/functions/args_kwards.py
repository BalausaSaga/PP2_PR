# 1.
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))

# 2.
def print_args(*args):
    for arg in args:
        print(arg)

print_args("apple", "banana", "cherry")

# 3.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Balausa", age=25, city="Almaty")

# 4.
def mixed(a, b, *args, **kwargs):
    print("a:", a, "b:", b)
    print("extra:", args)
    print("main:", kwargs)

mixed(1, 2, 3, 4, x=10, y=20)

# 5.
def configure(**options):
    return f"Configuration: {options}"

print(configure(debug=True, version="1.0"))