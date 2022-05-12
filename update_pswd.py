from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os,binascii
import pickle

directory = "/home/akshay/Desktop/Data app/New/"

filepath = directory + input("Enter filename whose password is to be changed: ")

#Reads the file
received_msg = pickle.load(open(filepath, 'rb'))

#Breaking down received message
received_ciphertext, received_tag, received_nonce, received_kdf_salt = received_msg

# Generate decryption key from passphrase and salt
decryption_passphrase = input("Enter the previous password: ")
decryption_key = PBKDF2(decryption_passphrase, received_kdf_salt)
#print ("Decryption Key: " + str(decryption_key))

# Validate MAC and decrypt
# If MAC validation fails, ValueError exception will be thrown
cipher = AES.new(decryption_key, AES.MODE_GCM, received_nonce)

try:
    decrypted_data = cipher.decrypt_and_verify(received_ciphertext, received_tag)
    new_pswd = input("\nPlease enter the new password for the file: ")
    
    #New key generation
    salt = get_random_bytes(16)
    key = PBKDF2(new_pswd, salt)
    
    #Encrypting data with new key
    new_data = str(decrypted_data)
    new_sensitive_data = str.encode(new_data)
    
    #AES Encryption
    # Encrypt using AES GCM
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(new_sensitive_data)
    # Nonce is generated randomly if not provided explicitly
    nonce = cipher.nonce
    
    transmitted_message = ciphertext, tag, nonce, salt
    pickle.dump(transmitted_message, open(filepath, 'wb'))
    print("\n Password updated successfully!")
    import new
    
    
except ValueError as mac_mismatch:
    print ("\n Incorrect password!!!")