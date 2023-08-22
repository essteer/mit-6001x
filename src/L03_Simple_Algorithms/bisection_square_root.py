# Approximate the square root of an int using bisection search

x = int(input("Enter an integer: "))

epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2

while abs(ans**2 - x) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print(f"number of guesses = {num_guesses}")
print(f"{ans} is close to square root of {x}")
