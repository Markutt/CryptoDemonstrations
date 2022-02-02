import random
import string


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
    enc_mapping = {}
    dec_mapping = {}
    seed = 5

    def generate(self):
        self.seed = input("Please enter a seed to be used in mapping, Press enter for default:")
        all_chars = string.printable
        shuffled_chars = list(all_chars)
        random.Random(self.seed).shuffle(shuffled_chars)
        enc_mapping: dict
        for char, s_char in zip(all_chars, shuffled_chars):
            self.enc_mapping[char] = s_char
            self.dec_mapping[s_char] = char

        # #Uncomment this chunk if you want to see the character mappings.
        # print("Character Mappings")
        # for count, (a, b) in enumerate(zip(list(all_chars), shuffled_chars)):
        #     print(f"[{a}]->[{b}]", end=" | ")
        #     count %= 10
        #     if count == 9:
        #         print()
        # print()

    def encrypt(self, plaintext):
        ciphertext = ""
        char_list = list(plaintext)
        for char in char_list:
            ciphertext += self.enc_mapping[char]
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        char_list = list(ciphertext)
        for char in char_list:
            plaintext += self.dec_mapping[char]
        return plaintext
