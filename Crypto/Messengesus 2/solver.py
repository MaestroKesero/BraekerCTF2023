with open("/dev/urandom","rb") as file:
    urandom = file.readlines()

print(len(urandom))