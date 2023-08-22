# Approximate the cube root of an int using bisection search

x = int(input("Enter an integer: "))

epsilon = 0.01
num_guesses, low = 0, 1
high = x
ans = (high + low) / 2.0

while abs(ans**3 - x) >= epsilon:
    print(f"low = {low}, high = {high}, ans = {ans}")
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print(f"number of guesses = {num_guesses}")
print(f"{ans} is close to cube root of {x}")
