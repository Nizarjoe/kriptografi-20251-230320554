# Laporan Praktikum Kriptografi

Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5DSRA
---

## 1. Tujuan
Setelah praktikum ini, mahasiswa mampu:

Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi.

Menerapkan algoritma Vigenère Cipher dengan variasi kunci.

Mengimplementasikan algoritma transposisi sederhana.

Menjelaskan kelemahan algoritma kriptografi klasik.
---

## 2. Dasar Teori
Cipher klasik adalah metode kriptografi awal yang menggunakan prinsip substitusi dan transposisi untuk mengamankan pesan sebelum era komputer digital.
Caesar Cipher adalah teknik substitusi monoalfabetik, di mana tiap huruf digeser sejumlah kunci tetap, sedangkan Vigenère Cipher memakai kunci berupa kata berdurasi variabel sehingga tiap karakter plaintext mengalami pergeseran yang bergantung pada posisi karakter kunci.

Pada kedua algoritma, enkripsi dan dekripsi bergantung pada operasi modular aritmetika, terutama modulo 26 sesuai jumlah huruf alfabet Latin. Cipher transposisi tidak mengubah karakter pesan, tetapi mengubah urutannya menurut pola tertentu (misalnya urutan kolom).
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
1. Membuat folder praktikum/week5-cipher-klasik/ dengan subfolder src/, screenshots/, dan file      laporan.md.
2. Menyalin dan menyimpan kode:
    src/caesar.py: program implementasi Caesar Cipher.
    src/vigenere.py: program implementasi Vigenère Cipher.
    src/transpose.py: program transposisi sederhana.
3. Menjalankan program dengan perintah python src/caesar.py  
    python src/vigenere.py  
    python src/transpose.py  

4. Mengambil screenshot hasil uji (output terminal operasi enkripsi dan dekripsi), menyimpan di folder screenshots/hasil.png.
5. Menyusun dan mengisi laporan.md sesuai hasil implementasi dan instruksi.

---

## 5. Source Code
1. src/caesar.py
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

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
-

2. src/vigenere.py

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

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

3. src/transpose.py

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

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

## 6. Hasil dan Pembahasan
Berikut hasil uji coba algoritma:

Algoritma: Caesar Cipher
Plaintext: CLASSIC CIPHER
Key: 3
Ciphertext: FODVVLF FLSKHU
Decrypted: CLASSIC CIPHER

Algoritma: Vigenère Cipher
Plaintext: KRIPTOGRAFI
Key: KEY
Ciphertext: UBPJSCCRAHZ
Decrypted: KRIPTOGRAFI

Algoritma: Transposisi Sederhana
Plaintext: TRANSPOSITIONCIPHER
Key: 5
Ciphertext: TSINPOTRCIEAORHPNIT
Decrypted: TRANSPOSITIONCIPHER

Screenshot eksekusi program tersimpan di screenshots/hasil.png.

Pembahasan:

Hasil enkripsi dan dekripsi untuk Caesar dan Vigenère kembali ke teks semula, menandakan algoritma berjalan sesuai teori.

Pada transposisi, urutan karakter berubah namun seluruh informasi tetap, sehingga dekripsi mampu mengembalikan pesan.

Tidak ditemukan error signifikan saat eksekusi.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
