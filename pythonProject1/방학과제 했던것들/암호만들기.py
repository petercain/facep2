cipher = {
    "a": "o", "b": "2", "c": "E", "d":"4", "e": "6", "f": "5", "g": "7", "h": "8", "i": "9", "j": "a", "k": "b",
    "l": "c", "m":"d", "n": "3", "o":"f", "p":"g", "q":"H", "r": "i", "s": "j", "t": "k", "u":"l", "v": "m", "w": "n", "x":"1","y":"p", "z": "q"
}


encryption = input("암호화")
for aa in range(len(encryption)):

    if encryption[aa] in cipher:
        print(cipher[encryption[aa]],end='')
print()

i = -1
decryption = input("해독")
order_1 = len(decryption)
for cc in range(order_1):
    i += 1
    for key, value in cipher.items():
        if value == decryption[i]:
            print(key,end='')





