import random
__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Monoalphabet:
    alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        lowercase_code = {x: y for x, y in zip(keytable, self.alphabet)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(keytable, self.alphabet)}
        self._decode = dict(lowercase_code)
        self._decode.update(uppercase_code)
    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])
        
key = list("эьормщднйгычясюцажшбтпвёлеъузхкфи")
cipher = Monoalphabet(key)
line = input()
while line != '.':
    print(cipher.decode(line))
    line = input()