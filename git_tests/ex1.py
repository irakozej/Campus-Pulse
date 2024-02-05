import random

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

print(f"Generated number: {random_number}")
result = check_even_odd(random_number)
print(f"The generated number is {result}.")
