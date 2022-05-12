print("Please seclect one of the following options: \n1. Encrypt \n2. Decrypt \n3. Upload file \n4. Integrity Check \n5. Download file \n6. Password Update")
opt = input()
if opt == "1":
	import aes_enc
elif opt == "2":
	import aes_dec
elif opt == "3":
	import new
elif opt == "4":
	import integrity_check
elif opt == "5":
	import download
elif opt == "6":
	import update_pswd
else:
	print("Invalid option!")
	