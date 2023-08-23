# An example of timing a program to test efficiency
# This is not an optimal method

import time


def celsius_to_fahrenheit(c):
    return c * 9/5 + 32


# time.clock() was removed in Python 3.8, after deprecation in version 3.3
# use time.perf_counter() or time.process_time() instead, according to requirements

t0 = time.perf_counter()
celsius_to_fahrenheit(100000)
t1 = time.perf_counter() - t0

print(f"t = {t0}:{t1} s,")

# Timing is a poor option, because of differents across platforms, environments, etc.
