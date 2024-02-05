def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

print(f"Generated number: {random_number}")
result = factorial(random_number)
print(f"The factorial of {random_number} is {result}.")

#recursive program that generates a random number and calculates it's factorial
