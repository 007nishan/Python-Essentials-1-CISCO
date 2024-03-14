text = "Natural Language Processing using Python"
words = text.split()
x = [len(word) for word in words]
y = sum(x)
z = y/len(x)
print(y,z)

print(x)