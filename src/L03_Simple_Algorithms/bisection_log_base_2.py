# Approximate the log base 2 of an int using bisection search

x = int(input("Enter an integer: "))

epsilon = 0.01
# find lower bound on ans
lower_bound = 0

while 2**lower_bound < x:
    lower_bound += 1

low = lower_bound - 1
high = lower_bound + 1

# perform bisection search
ans = (high + low) / 2

while abs(2**ans - x) >= epsilon:
    if 2**ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print(f"{ans} is close to the log base 2 of {x}")
