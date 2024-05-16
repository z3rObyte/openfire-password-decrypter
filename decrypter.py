from Crypto.Cipher import Blowfish
from Crypto.Hash import SHA1
from Crypto.Util.Padding import unpad
import binascii
import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} encryptedPassword Key")
    sys.exit(1)

def decrypt_openfirepass(ciphertext, key):
    sha1_key = SHA1.new(key.encode('utf-8')).digest()
    ciphertext_bytes = binascii.unhexlify(ciphertext)
    block_size = Blowfish.block_size
    iv = ciphertext_bytes[:block_size]
    ciphertext_data = ciphertext_bytes[block_size:]
    cipher = Blowfish.new(sha1_key, Blowfish.MODE_CBC, iv)
    plaintext_padded = cipher.decrypt(ciphertext_data)
    plaintext = unpad(plaintext_padded, block_size)
    
    return plaintext.decode('utf-8')

print(f"Decrypted password: {decrypt_openfirepass(sys.argv[1], sys.argv[2])}")
