def ceasar(encode_or_decode, original_text, shift_amnt):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

    output_text = ""
    for letter in original_text:

        if letter in alphabet:
            if encode_or_decode == "encode":
                idx = alphabet.index(letter) + shift_amnt
            else:
                idx = alphabet.index(letter) - shift_amnt
            idx %= len(alphabet)
            output_text += alphabet[idx]
            
        else:
            output_text+=letter

    return output_text


command = "yes"
while command == "yes":
    direction = input("Type 'encode' to encrypt and type 'decode' to decrypt: ").lower()
    original_text = input("Type your message: ").lower()
    shift_amnt = int(input("Type the shift number: "))

    cipher_text = ceasar(direction, original_text, shift_amnt)

    print(f"Here's your {direction}d result: {cipher_text}")
    command = input("Type 'yes' if you wanna go again. Otherwise type 'no': ").lower()
    
