hello="Hello world"

print(hello)
with open("content.txt", "w") as file:
    file.write(hello)