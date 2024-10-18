friends = 10

# friends=friends+1
# friends+=1

# friends=friends-2
# friends-=2

# friends=friends*3
# friends*=3

# friends=friends/2
# friends/=2

# friends=friends**2  # exponential
# friends**=2

# friends = friends % 2

# print(friends)


x = 3.56
y = -4
z = 5
"""
print(round(x))
print(abs(y))
print(pow(4, 3))
print(max(x, y, z))
print(min(x, y, z))
"""

import math

p = 9.9

print(math.pi)
print(round(math.pi, 2))
print(math.sqrt(p))
print(math.ceil(p))
print(math.floor(p))


# calculate c= √(a²+b²)  # alt+0178=square

a = float(input(f"Enter value of a: "))
b = float(input(f"Enter value of b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Value of c: {c}")
