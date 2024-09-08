alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def print_menu():
    print("Do you want to encode? Type 1")
    print("Do you want to decode? Type 2")



def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)
            encoded_message += alphabet[new_position]
    return encoded_message

def decode(message, shift):
    decoded_message = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % len(alphabet)
            decoded_message += alphabet[new_position]
    return decoded_message


while True:
    print_menu()
    user_command = int(input())
    user_shift = int(input("Type the shift number: ")) % 26
    user_message = input("Type your message to encode or decode: ")

    if user_command == 1:
        print(encode(user_message, user_shift))
    elif user_command == 2:
        print(decode(user_message, user_shift))
    else:
        print("Invalid command")

    repeat = input("Do you want to encode or decode again? Type 'yes' or 'no': ")
    if repeat == "no":
        print("Thanks for using this application")
        break
    elif repeat == "yes":
        continue
    else:
        print("Invalid command")
        break