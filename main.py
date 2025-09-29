alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

checking = False
while checking == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        checking = True
    elif text == int or shift == str:
        checking = True
    else:
        print("Invalid Direction/Message/Shift.")

def encrypt(original_text, shift_amount):
    encrypted = ""

    for letter in original_text:
        number = alphabet.index(letter) + shift_amount
        number %= len(alphabet)

        if direction == "decode":
            number = alphabet.index(letter) - shift_amount
        elif direction == "encode":
            encrypted += alphabet[number]

    print(encrypted)

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        number = alphabet.index(letter) - shift_amount
        number %= len(alphabet)

        cipher_text += alphabet[number]

    print(f"Here is the decoded result: {cipher_text}")

def ceasar(text_, shift_, direction_):
    if direction_ == "encode":
        encrypt(text_,shift_)
    elif direction_ == "decode":
        decrypt(text_,shift_)

ceasar(text, shift)