import ssl
import nltk
from nltk.corpus import words, names

alphabet = ['a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z']


def encrypt(plain_text, key):
    shifted = ''
    phrase = str(plain_text)

    for char in phrase:
        if char.lower() in alphabet:
            char_idx = alphabet.index(char.lower())
            shifted_char_idx = (char_idx + key) % 26
            if char == char.lower():
                shifted += alphabet[shifted_char_idx]
            else:
                shifted += alphabet[shifted_char_idx].upper()
        else:
            shifted += char
    return shifted


def decrypt(encrypted, key):
    return encrypt(encrypted, -key)


def crack(encrypted_msg):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("words", quiet=True)
    nltk.download('names', quiet=True)

    word_list = words.words()
    name_list = names.words()

    for i in range(26):
        counter = 0
        msg = encrypt(encrypted_msg, i)
        msg_list = msg.split()

        for txt in msg_list:
            if txt.lower() in word_list or txt.lower() in name_list:
                counter += 1
        if (counter/len(msg_list)) > .6:
            return ' '.join(msg_list)
    return ''
