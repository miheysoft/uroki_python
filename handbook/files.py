# открытие файла в режиме чтения
with open("if_mount.sh") as f:
    contents = f.read()
    print(contents)
    print(type(contents))

# чтение файла по частям
with open("if_mount.sh", "r") as f:
    for line in f:
        print(line)
print(type(line))


# чтение файла по частям по 100 байт за раз
with open("if_mount.sh", "r") as f:
    while True:
        chunk = f.read(10)
        if not chunk:
            break
        print(chunk)
print(type(chunk))

# запись файла
with open("example.txt", "w") as f:
    f.write("Hello, world!")
