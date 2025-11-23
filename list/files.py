# data = input("Enter text: ")
#
# file = open('C:/Users/astonuser/PycharmProjects/pythonProject/data/text.txt', 'w')
#
# file.write(data + "\n")
#
# file.close()

# file = open('C:/Users/astonuser/PycharmProjects/pythonProject/data/text.txt', 'r')

# print(file.read())

# for line in file:
#     print(line)
#
# file.close()

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")