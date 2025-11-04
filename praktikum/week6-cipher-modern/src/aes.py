from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce, ciphertext, tag

def decrypt_aes(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted

def main():
    print("=== Implementasi AES-128 ===")
    key = get_random_bytes(16)  # 128-bit key
    print("Kunci (hex):", binascii.hexlify(key).decode())

    plaintext = b"AES Example with 128-bit Key"
    print("Plaintext:", plaintext.decode())

    nonce, ciphertext, tag = encrypt_aes(plaintext, key)
    print("Nonce (hex):", binascii.hexlify(nonce).decode())
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())
    print("Tag (hex):", binascii.hexlify(tag).decode())

    decrypted = decrypt_aes(nonce, ciphertext, tag, key)
    print("Hasil Dekripsi:", decrypted.decode())

if __name__ == "__main__":
    main()
