import random
import re

replace_space = "fghFGH"
insert_between_letter = "cvbCVB"
all_letters = "adeijklmnopqrstuwxyzADEIJKLMNOPQRSTUXYZ!@#$%^&*(),.?/"

def encrypt_func(og_message, key):
    encrypted_message = ""
    
    for letter in og_message.replace(".", "").replace(",", ""):
        if len(encrypted_message) % 3 == 0:
            rand_all_letters = random.choice(all_letters)
            encrypted_message += rand_all_letters
        if letter == " ":
            rand_replace_space = random.choice(replace_space)
            encrypted_message += rand_replace_space
        if letter != " ":
            rand_insert_between_letter = random.choice(insert_between_letter)
            encrypted_message += rand_insert_between_letter
          
        enc_letter = ord(key[0]) + ord(key[1]) + ord(key[4]) + ord(key[5])
        encrypted_message += str(ord(letter) + enc_letter)
    
    if ord(key[2]) >= 90:
        return encrypted_message[::-1]
    else:
        return encrypted_message
    
    
def decrypt_func(enc_message, key):
    decrypted_message = ""
    
    if ord(key[2]) >= 90:
        enc_message = enc_message[::-1]
        
    for letter in enc_message:
        if letter in all_letters:
            enc_message = enc_message.replace(letter, "")
        elif letter in replace_space:
            enc_message = enc_message.replace(letter, " ")
        
    split_enc_message = re.split(r"[cvbCVB ]", enc_message)
    split_enc_message = [i for i in split_enc_message if i != " "]
    
    for i in split_enc_message:
        if i.isdigit():
            enc_letter = ord(key[0]) + ord(key[1]) + ord(key[4]) + ord(key[5])
            decrypted_message += chr(int(i) - enc_letter)

    return decrypted_message


if __name__ == "__main__":
    while True:
        print("=" * 85)
        key = input("Enter a 6 character master key (can include letters, numbers, and special characters): ")

        if len(key) != 6:
            print("Please enter exactly six characters.\n")
            continue
        else:
            print("\n1. Encrypt\n2. Decrypt\n")
            
            selected_option = int(input("Select a option (1 or 2): "))
            if selected_option == 1:
                original_message = input("Enter a message to encrypt: ")
                encrypted = encrypt_func(original_message, key)
                print(f"Encrypted Message: {encrypted}\n")
            elif selected_option == 2:
                encrypted_message = input("Enter a message to decrypt: ")
                decrypted = decrypt_func(encrypted_message, key)
                print(f"Decrypted Message: {decrypted}\n")