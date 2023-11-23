alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 3

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
#     print(f"Message encrypté >>> {CesarEncrypt(message, key)}")

# elif choice == 2:
#     print("")
#     message = input("Message >>> ")
#     print(f"Message decrypté >>> {CesarDecrypt(message, key)}")


## Ces tests unitaires fonctionne uniquement si key = 3
assert CesarEncrypt("abc", key) == "def"
assert CesarEncrypt("xyz", key) == "abc"
assert CesarEncrypt("coucou", key) == "frxfrx"

assert CesarDecrypt("def", key) == "abc"
assert CesarDecrypt("abc", key) == "xyz"
assert CesarDecrypt("frxfrx", key) == "coucou"