# sum_of_multiples.py

# Project Euler Problem 1:
# Find the sum of all the natural numbers below 1000
# that are multiples of 3 or 5.

# We'll use a simple loop and a conditional to check if
# each number from 1 to 999 is divisible by 3 or 5,
# and then keep a running total.

# Initialize a variable to keep track of the total sum
total = 0

# Loop through all numbers from 1 up to (but not including) 1000
for number in range(1, 1000):
    # Check if the current number is divisible by 3 or 5
    if number % 3 == 0 or number % 5 == 0:
        total += number  # Add the number to the total if condition is true

# After the loop ends, print the result
print("The sum of all the multiples of 3 or 5 below 1000 is:", total)
