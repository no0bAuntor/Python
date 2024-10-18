import time

countdown = int(input("Enter countdown times: "))
"""
for x in range(1, countdown):
               print(x)
               time.sleep(1)
"""


# In reverse order
for x in reversed(range(0, countdown)):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print("Times up")

