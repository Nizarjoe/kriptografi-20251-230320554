from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(plaintext, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted

def main():
    print("=== Implementasi RSA 2048-bit ===")
    private_key, public_key = generate_keys()

    print("Kunci Publik:\n", public_key.decode()[:200], "...")
    print("Kunci Privat:\n", private_key.decode()[:200], "...")

    plaintext = b"RSA Encryption Test Message"
    print("Plaintext:", plaintext.decode())

    ciphertext = encrypt_rsa(plaintext, public_key)
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode()[:120], "...")

    decrypted = decrypt_rsa(ciphertext, private_key)
    print("Hasil Dekripsi:", decrypted.decode())

if __name__ == "__main__":
    main()
