from my_library import *
print("1. ***")
print("   ***")
print("   ***")
print("2.  * ")
print("   ***")
print("    * ")
print("3. 999")
print("   888")
print("   777")
print("4. 111")
print("   222")
print("   333")
a = int(input("Введите цифру от 1 до 4: "))



if a == 1:
    print(first())
if a == 2:
    print(second())
if a == 3:
    print(third())
if a == 4:
    print(four())