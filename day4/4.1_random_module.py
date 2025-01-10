import random
import my_module  # Use the correct module name

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.randint(0, 5)
print(random_float)
# Accessing a variable from the imported module
print(my_module.name)
