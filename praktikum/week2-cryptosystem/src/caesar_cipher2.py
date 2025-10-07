def encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) - 48 + key) % 10 + 48)
        else:
            result += char
    return result


def decrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) - 48 - key) % 10 + 48)
        else:
            result += char
    return result


if __name__ == "__main__":
    print("=== PILIH MODE ===")
    print("1. Mode Langsung (pesan sudah ada di dalam kode)")
    print("2. Mode Input (pesan diketik manual)")
    mode = input("Pilih mode (1/2): ")

    if mode == "1":
        # 🔹 Mode langsung: pesan & kunci ditulis di sini
        message = "MUHAMMAD NIZAR ASAGAF 230320554"
        key = 4
        print("\n--- Mode Langsung ---")

    elif mode == "2":
        # 🔹 Mode input: pesan & kunci dimasukkan saat program dijalankan
        message = input("\nMasukkan pesan: ")
        key = int(input("Masukkan kunci (angka): "))
        print("\n--- Mode Input ---")

    else:
        print("Pilihan tidak valid!")
        exit()

    # 🔍 Info tambahan
    print("\nKunci huruf yang digunakan :", key % 26)
    print("Kunci angka yang digunakan :", key % 10)

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("\n=== HASIL ===")
    print("Plaintext  :", message)
    print("Ciphertext :", encrypted)
    print("Decrypted  :", decrypted)
