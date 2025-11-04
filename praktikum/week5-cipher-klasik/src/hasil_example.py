# ====================================================
# Praktikum Minggu 5 - Cipher Klasik
# Caesar, Vigenere, dan Transposisi
# ====================================================

# === Caesar Cipher ===
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)


# === Vigenere Cipher ===
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


# === Transposisi Cipher ===
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)


# === Menu Interaktif ===
def main():
    print("="*50)
    print("🔐 PRAKTIKUM: CIPHER KLASIK (Caesar, Vigenere, Transposisi)")
    print("="*50)

    print("\nPilih algoritma:")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Transposisi Cipher")

    choice = input("Masukkan pilihan (1/2/3): ").strip()

    if choice == "1":
        text = input("Masukkan teks: ")
        key = int(input("Masukkan kunci (angka): "))
        enc = caesar_encrypt(text, key)
        dec = caesar_decrypt(enc, key)
        print("\n[Caesar Cipher]")
        print(f"Ciphertext: {enc}")
        print(f"Decrypted : {dec}")

    elif choice == "2":
        text = input("Masukkan teks: ")
        key = input("Masukkan kunci (kata): ")
        enc = vigenere_encrypt(text, key)
        dec = vigenere_decrypt(enc, key)
        print("\n[Vigenere Cipher]")
        print(f"Ciphertext: {enc}")
        print(f"Decrypted : {dec}")

    elif choice == "3":
        text = input("Masukkan teks: ")
        key = int(input("Masukkan kunci (angka): "))
        enc = transpose_encrypt(text, key)
        dec = transpose_decrypt(enc, key)
        print("\n[Transposisi Cipher]")
        print(f"Ciphertext: {enc}")
        print(f"Decrypted : {dec}")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
