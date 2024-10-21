# dictionary= a collection of {key:value} pairs ordered and changeable. No duplicates

capitals={"USA": "Washington D.C",
          "India": "New Delhi",
          "China": "Beijing",
          "Russia": "Moscow"}

print(capitals.get("USA"))

capitals.update({"Germany": "Berlin"})
capitals.pop("China")

print(capitals)

keys=capitals.keys()
print(keys)

for values in capitals.values():
    print(values)

for key, value in capitals.items():
    print(f"{key}: {value}")    