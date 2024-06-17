from Crypto.Cipher import AES #pycryptodome
#I allowed disabling verification because it *MIGHT* increase processing power to bruteforce this. e.g. detecting sensable data in decrypted file is harder than verificating decrypted message
def encrypt(key, plaintext, partial_return = False, verify = True):
	cipher = AES.new(key, AES.MODE_EAX)
	nonce = cipher.nonce
	ciphertext, tag = cipher.encrypt_and_digest(plaintext)
	if verify:
		return b"".join([tag, nonce, ciphertext]) if not partial_return else (tag, nonce, ciphertext)
	else:
		return b"".join([nonce, ciphertext]) if not partial_return else (nonce, ciphertext)

def decrypt(key, ciphertext, verify = True):
	if verify:
		tag = ciphertext[0:16]
		nonce = ciphertext[16:32]
		ciphertext = ciphertext[32:]
	else:
		nonce = ciphertext[0:16]
		ciphertext = ciphertext[16:]
	cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	if verify:
		cipher.verify(tag)
	return plaintext
