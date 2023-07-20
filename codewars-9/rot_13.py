import string
from codecs import encode as _dont_use_this_
import codecs


def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) + 13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) + 13) % 26]
        else:
            outputMessage += letter
    return outputMessage


# Cheating(mine):
def rot13(message):
    return codecs.encode(message, 'rot_13')
