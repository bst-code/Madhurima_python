name = "python programming"

size = len(name)

print(size)

print("python programming".upper())
print(name.lower())
print(name.capitalize())
print(name.title())

language = "   i learn java  "
print(language)

print(language.strip())
print(language.lstrip())

print(language.rstrip())


print(language.replace("java", "python"))

spaceRemovedData = language.strip() #i learn java
print(spaceRemovedData.find("a"))

print(spaceRemovedData.count("a"))
spaceRemovedData = "Bala123"
print(spaceRemovedData.isalnum())
print(spaceRemovedData.isalpha())
print(spaceRemovedData.isnumeric())
print(spaceRemovedData.isdigit())

print(spaceRemovedData.startswith("Ba"))
print(spaceRemovedData.endswith("3"))
