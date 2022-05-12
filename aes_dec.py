from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os,binascii
import pickle

import download
# Decryption step
# The receiver code begins here
#Store data to a file
# path of this script
directory = "/home/akshay/Desktop/Data app/Download/"

# get fileName from user
filepath = directory + input("Enter filename to read: ")

# Reads the file
received_msg = pickle.load(open(filepath, 'rb'))

#Breaking down received message
received_ciphertext, received_tag, received_nonce, received_kdf_salt = received_msg

# Generate decryption key from passphrase and salt
decryption_passphrase = input("Enter decryption passphrase: ")
decryption_key = PBKDF2(decryption_passphrase, received_kdf_salt)
#print ("Decryption Key: " + str(decryption_key))

# Validate MAC and decrypt
# If MAC validation fails, ValueError exception will be thrown
cipher = AES.new(decryption_key, AES.MODE_GCM, received_nonce)

try:
    decrypted_data = cipher.decrypt_and_verify(received_ciphertext, received_tag)
    print ("\nMAC validated: Data was encrypted by someone with the shared secret passphrase")
    print ("All allies have passphrase - SYMMETRIC encryption!!!")
    print ("Decrypted sensitive data: " + str(decrypted_data))
except ValueError as mac_mismatch:
    print ("\nMAC validation failed during decryption. No authentication gurantees on this ciphertext")