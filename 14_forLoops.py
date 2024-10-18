print("Count 1 to 10:")
for x in range(1, 11):
    print(x)

print("Count 10 to 11:")
for x in reversed(range(1, 11)):
    print(x, end="")

print("Count 1 to 10 with 2 step:")
for x in range(1, 11, 2):
    print(x)

print("Skip 13")    
for x in range(1,20):
    if x==13:
        continue
    print(x)

