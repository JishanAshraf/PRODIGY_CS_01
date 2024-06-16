def caesar_cipher(text, shift, mode='encrypt'):

    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for char in text:
        if char not in alphabet:
            result += char
            continue

        new_index = (alphabet.index(char) + shift) % len(alphabet)
        new_char = alphabet[new_index]

        if mode == 'encrypt':
            result += new_char
        elif mode == 'decrypt':
            result += new_char
        else:
            raise ValueError("Invalid mode: {}".format(mode))

    return result

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice in ('1', '2'):
            text = input("Enter the text: ")
            shift = int(input("Enter the shift amount: "))

            if choice == '1':
                encrypted_text = caesar_cipher(text, shift)
                print("Encrypted text:", encrypted_text)
            else:
                decrypted_text = caesar_cipher(text, -shift, mode='decrypt')
                print("Decrypted text:", decrypted_text)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

