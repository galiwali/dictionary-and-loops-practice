# this is what we will use for the video intro to dictionaries

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Japan"))
if capitals.get("Japan"):
    print("That capital exists")
else:
    capitals.update({"Germany":"Berlin"})
    capitals.update({"USA": "Detroit"})
    capitals.pop("China")
    capitals.popitem()
    capitals.clear()

keys= capitals.keys()
print(keys)
print(capitals)
for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)
items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}:{value}")