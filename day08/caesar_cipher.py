"""Caesar's cipher in Python, Caesar's Pypher😂"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(cipher_type, start_text, shift_amt):
    """Defines a simple implementation of the famous
    Caesar's cipher functionality

    Args:
        cipher_type (str): the direction of the cipher; encode or decode
        shift_amt (int): the number of times to shift the message
        start_text (str): the starting message to encode/decode
    Returns:
        the encoded/decoded message
    """

    end_text = ""

    if cipher_type == 'decode':
        shift_amt *= -1  # to shift in reverse direction

    for char in start_text:
        if char in alphabet:
            # to avoid error with symbols and numbers, only
            # shifting letters in alphabet
            pos = alphabet.index(char)
            new_pos = pos + shift_amt
            new_char = alphabet[new_pos]
            end_text += new_char
        else:
            end_text += char
    return "Your {}d message is {}".format(cipher_type, end_text)


direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

message = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


final_message = caesar(direction, message, shift)
print(final_message)
