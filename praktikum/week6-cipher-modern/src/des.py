from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

# Fungsi untuk menyesuaikan panjang plaintext ke kelipatan 8 byte
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def main():
    print("=== Implementasi DES ===")
    key = get_random_bytes(8)  # 64-bit key (8 byte)
    print("Kunci (hex):", binascii.hexlify(key).decode())

    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = b"DES Encryption Example"
    padded_text = pad(plaintext)

    ciphertext = cipher.encrypt(padded_text)
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())

    # Dekripsi
    decipher = DES.new(key, DES.MODE_ECB)
    decrypted = decipher.decrypt(ciphertext).rstrip()
    print("Hasil Dekripsi:", decrypted.decode())

if __name__ == "__main__":
    main()
