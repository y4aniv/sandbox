alphabet = "abcdefghijklmnopqrstuvwxyz"

def CesarEncrypt(text, key):
    """Encrypte le message en utilisant le chiffrement César
    Entrée: text (str)
    Sortie: result (str)
    """
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            result += char
    return result

def CesarDecrypt(text, key):
    """Decrypte le message en utilisant le chiffrement César
    Entrée: text (str)
    Sortie: result (str)
    """
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char in alphabet:
            result += alphabet[(alphabet.index(char) - key) % len(alphabet)]
        else:
            result += char
    return result

# print("Encrypter un message (1)")
# print("Decrypter un message (2)")
# print("")

# choice = int(input(">>> "))

# if choice == 1:
#     print("")
#     message = input("Message >>> ")
#     key = int(input("Clé >>> "))
#     print(f"\nMessage encrypté >>> {CesarEncrypt(message, key)}")

# elif choice == 2:
#     print("")
#     message = input("Message >>> ")
#     key = int(input("Clé >>> "))
#     print(f"\nMessage decrypté >>> {CesarDecrypt(message, key)}")


assert CesarEncrypt("abc", 4) == "efg"
assert CesarEncrypt("xyz", 9) == "ghi"
assert CesarEncrypt("Coucou, comment ça va ?", 5) == "Ctzhtz, htrrjsy çf af ?"

assert CesarDecrypt("efg", 4) == "abc"
assert CesarDecrypt("ghi", 9) == "xyz"
assert CesarDecrypt("Ctzhtz, htrrjsy çf af ?", 5) == "Coucou, comment ça va ?"