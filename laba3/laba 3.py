# n = open('example.txt', 'r')
# print(*n)
# n.close()

#Чтение всего файла
with open('example.txt', 'r') as n:
    contet = n.read()
    print(contet)

#Построчнео чтение
# with open('example.txt', 'r') as n:
#     for line in n:
#         print(line)

# a = input("Enter the text:")
# with open("user_input.txt", "w") as n:
#     n.write(a)

# a = input("Enter the text:")
# with open("user_input.txt", 'a') as n:
#     n.writelines(a)
# try:
#     a = input("Enter the file name:")
#     with open("a", 'r') as n:
#         content = n.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found")

# print("Hello")