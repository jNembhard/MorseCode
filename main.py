# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',   '-': '-....-',   '(': '-.--.', ')': '-.--.-'
    }

ENGLISH_TO_MORSE = {value: key for key, value in MORSE_CODE_DICT.items()}


def morse_code(encryption):
    return ' '.join(MORSE_CODE_DICT.get(char.upper()) for char in encryption)


def english_code(decryption):
    if decryption in ENGLISH_TO_MORSE.keys():
        return ''.join(ENGLISH_TO_MORSE.get(char) for char in decryption.split())
    else:
        return False


def message():
    while True:
        word = input("Type 'E' to encrypt morse code message or 'M' to decrypt morse code message: ").upper()
        if not (word == 'E' or word == 'M'):
            print("Invalid command!\n")
            continue
        else:
            break

    if word == 'E':
        word = input("Type your message in English: ")
        print(morse_code(word))

    elif word == 'M':
        while True:
            word = input("Type your message in morse code: ")
            phrase = english_code(word)
            if not phrase:
                phrase = 'M'
                print("Invalid Command!\n")

            else:
                print(phrase)
                break


message()
