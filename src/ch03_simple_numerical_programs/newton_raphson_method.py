# Newton-Raphson method for finding the square root of an int

k = int(input("Enter an integer: "))

# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
guess = k / 2
num_guesses = 0

while abs(guess**2 - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k) / (2*guess))

print(f"Square root of {k} is about {guess}")
print(f"Number of guesses is {num_guesses}")
