from binascii import hexlify
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.SecretSharing import Shamir

def secret_sharing(key):  # Accepts key as input from aes_enc
	#print(key)
	#key = b'\xa21]NUD\xe1\x0b\xbaY\xca\\\xe6\xe0~\xfd'
	min_req = int(input("Input the minimum no of people required to reassemble the key: "))
	splits = int(input("Enter the number of splits to be made of key: "))
	shares = Shamir.split(min_req, splits, key)
	for idx, share in shares:
		print("Index #%d: %s" % (idx, hexlify(share)))
	print("\n\n\n")

	from share_key_decrypt import key_assemble
	key_assemble(min_req, key)

