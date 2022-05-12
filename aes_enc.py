from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import os,binascii
import pickle

# Authenticated encryption on a string using AES GCM with both encryption and MAC

# Key generation
salt = get_random_bytes(16)
user_pswd = input("SECRET PASSPHRASE INPUT\nYou will need this to decrypt\nEnter secret passphrase: ")
key = PBKDF2(user_pswd, salt)
#key_hex = key.hex()
#print(key)


# Sensitive data to encrypt
user_data = input("\n\nSENSITIVE DATA INPUT\nEnter sensitive data to encrypt: ")
sensitive_data = str.encode(user_data)
print ("Sensitive data encrypted: " + (user_data))


# Encrypt using AES GCM
cipher = AES.new(key, AES.MODE_GCM)
#cipher.update(auth)
ciphertext, tag = cipher.encrypt_and_digest(sensitive_data)
# Nonce is generated randomly if not provided explicitly
nonce = cipher.nonce

# Print all the components of the message
print ("\nCOMPONENTS OF TRANSMITTED MESSAGE")
print ("\nCiphertext: " + str(ciphertext))
print ("\nAuthentication tag: " + str(tag))
print ("\nNonce: " + str(nonce))
print ("\nSalt: " + str(salt))

# Message to transmit/share
transmitted_message = ciphertext, tag, nonce, salt

#Store data to a file
# path of this script
directory = "/home/akshay/Desktop/Data app/New/"

# get fileName from user
filepath = directory + input("\nEnter filename to write: ")

# Creates a new file
pickle.dump(transmitted_message, open(filepath, 'wb'))

#upload file
user_opt = input("Do you wish to upload the encrypted file to cloud? (Y/n)")
if user_opt == "Y":
	import new
elif user_opt == "n":
	print("Okay. Thank you!")
else:
	print("Invalid option!")
	
#Shamir secret sharing
ss = input("Do you wish to share the secret key among members? (Y/n)")
if ss == "Y":
	from share_key import secret_sharing
	secret_sharing(key)
	
