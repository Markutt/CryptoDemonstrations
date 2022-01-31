class VigenereCipher:
    def encrypt(self):
        print("geldi")
        return

    def decrypt(self):
        return


class CaesarCipher:
    def encrypt(self, plaintext):
        return "".join(chr(ord(char) + 3) for char in plaintext)

    def decrypt(self, ciphertext):
        return "".join(chr(ord(char) - 3) for char in ciphertext)


class SubstitutionCipher:
    def encrypt(self):
        return

    def decrypt(self):
        return
