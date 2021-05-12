#FileNotFound

# try:
#     file = open("file.txt")
#     dict = {"key": "value"}
#     print(dict["dffefwef"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("write something")
# except KeyError as error_message:
#     print()
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     # finally works when you want some results regardless success or fail.

height = float(input("Height: "))
weight = int(input("Height: "))

if height > 3:
    raise ValueError("height is too big.")