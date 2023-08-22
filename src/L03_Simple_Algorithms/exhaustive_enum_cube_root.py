# Find the cube root of a perfect cube

# This programme uses exhaustive enumeration, a variant of guess-and-check

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(f"{x} is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print(f"Cube root of {x} is {ans}")
