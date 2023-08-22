# Approximate the square root of an int using exhaustive enumeration

# This programme uses exhaustive enumeration, a variant of guess-and-check

x = int(input("Enter an integer: "))

epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1

print(f"number of guesses = {num_guesses}")

if abs(ans**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")

else:
    print(f"{ans} is close to square root of {x}")
