def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Apply the shift and handle wrap-around
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            
            result += shifted_char
        else:
            result += char

    return result

def decrypt(text, shift):
    # Decryption is just encryption with a negative shift
    return encrypt(text, -shift)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print(f"\nEncrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
