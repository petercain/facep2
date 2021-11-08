list_a = [ "jj", "peter", "dorothy"]

for i in list_a:
    print(i.rjust(10))


for i in list_a:
    print(i.ljust(10))


for i in list_a:
    print(i.center(10))

# print(len("abc"))
#
# cipher = {
#     "a": "o", "b": "2", "c": "E", "d":"4", "e": "6", "f": "5", "g": "7", "h": "8", "i": "9", "j": "a", "k": "b",
#     "l": "c", "m":"d", "n": "3", "o":"f", "p":"g", "q":"H", "r": "i", "s": "j", "t": "k", "u":"l", "v": "m", "w": "n", "x":"1","y":"p", "z": "q"
# }
#
#
# encryption = input("암호화")
# order = len(encryption)
# for i in range(order):
#     if encryption[i] in cipher:
#         print(cipher[encryption[i]],end='')
# print()
#
# decryption = input("해독")
# order = len(decryption)
# for f in range(order):
#     for key, value in cipher.items():
#         if value == decryption[f]:
#             print(key,end='')