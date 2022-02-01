class VigenereCipher:
    key = "vigenere"

    def generate(self):
        user_input = input("Please enter the desired string key, Press Enter for default:")
        if user_input != "":
            self.key = user_input

    def encrypt(self, plaintext):
        pos = 0
        ciphertext = ""
        for char in plaintext:
            pos = pos % len(self.key)
            ciphertext += (chr(ord(char) + ord(self.key[pos])))
            pos += 1
        return ciphertext

    def decrypt(self, ciphertext):
        pos = 0
        plaintext = ""
        for char in ciphertext:
            pos = pos % len(self.key)
            plaintext += (chr(ord(char) - ord(self.key[pos])))
            pos += 1
        return plaintext


class CaesarCipher:
    shift_key = 3

    def generate(self):
        while True:
            user_input = input("Please enter the desired shift key, Press Enter for default:")
            if user_input == "":
                break
            elif user_input.isdigit():
                self.shift_key = int(user_input)
                break
            else:
                print("Please enter an integer")

    def encrypt(self, plaintext):
        return "".join(chr(ord(char) + self.shift_key) for char in plaintext)

    def decrypt(self, ciphertext):
        return "".join(chr(ord(char) - self.shift_key) for char in ciphertext)


class SubstitutionCipher:
    def encrypt(self):
        return

    def decrypt(self):
        return
