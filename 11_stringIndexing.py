creditNumber="1234-5678-2541"
print(creditNumber[4])

# [start:end]

print(creditNumber[:4])
print(creditNumber[5:9])
print(creditNumber[5:])
print(creditNumber[-1])  # last index
last4Digits=creditNumber[-4:]
print(f"XXXX-XXXX-{last4Digits}")


# [start:end:step]
print(creditNumber[::2]) # step 2 from beginning to end
print(creditNumber[5:10:2])

