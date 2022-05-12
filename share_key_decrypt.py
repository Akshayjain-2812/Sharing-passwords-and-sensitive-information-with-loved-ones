from binascii import unhexlify
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.SecretSharing import Shamir


def key_assemble(min_req,orig_key):
	import download
	shares=[]
	for x in range(min_req):
		in_str = input("\nEnter index and share separated by comma: ")
		#idx, share = [strip(s) for s in in_str.split(",") ]
		idx, share = in_str.split(",")
		i = int(idx)
		s = bytes.fromhex(share)
		shares.append((i, s))
	key = Shamir.combine(shares)
	if (key == orig_key):
		import aes_dec
	else:
		print("Error! Incorrect shares given!!")
