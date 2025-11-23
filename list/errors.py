# x = 0
# while x == 0:
#     try:
#         x = int(input("enter num: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print('need a number')

try:
    x = 5/0
except ZeroDivisionError:
    print("no")
except ValueError:
    print("need a number")
finally:
    print("finally")