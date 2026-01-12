# Laporan Praktikum Kriptografi

Minggu ke-: X
Topik: Implementasi Caesar Cipher
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5DSRA

---

## 1. Tujuan

Tujuan dari praktikum ini adalah untuk memahami konsep dasar kriptografi klasik menggunakan algoritma Caesar Cipher serta mampu mengimplementasikan proses enkripsi dan dekripsi sederhana menggunakan bahasa pemrograman Python.

---

## 2. Dasar Teori

Kriptografi merupakan ilmu yang mempelajari teknik pengamanan informasi dengan cara mengubah data asli (plaintext) menjadi data tersandi (ciphertext) agar tidak dapat dibaca oleh pihak yang tidak berwenang. Salah satu teknik kriptografi klasik yang paling sederhana adalah Caesar Cipher.

Caesar Cipher adalah metode substitusi di mana setiap huruf pada plaintext digeser sejauh nilai kunci tertentu dalam alfabet. Teknik ini menggunakan konsep aritmetika modulo, yaitu ketika pergeseran melewati huruf terakhir alfabet, maka perhitungan akan kembali ke awal alfabet.

Meskipun Caesar Cipher tidak aman untuk penggunaan modern, algoritma ini sangat bermanfaat sebagai media pembelajaran awal untuk memahami prinsip dasar enkripsi, dekripsi, dan penggunaan kunci dalam kriptografi.

---

## 3. Alat dan Bahan

* Python 3.x
* Visual Studio Code atau editor teks lainnya
* Git dan akun GitHub
* Sistem operasi Windows/Linux/macOS

---

## 4. Langkah Percobaan

1. Membuat folder project dengan nama `praktikum-kriptografi`.
2. Membuat file `caesar_cipher.py` di dalam folder project.
3. Menuliskan kode program Caesar Cipher menggunakan bahasa Python.
4. Menjalankan program melalui terminal dengan perintah `python caesar_cipher.py`.
5. Mengamati hasil enkripsi dan dekripsi yang dihasilkan program.
6. Melakukan commit hasil praktikum ke repository GitHub.

---

## 5. Source Code

Berikut adalah source code utama program Caesar Cipher:

```python
# Program Caesar Cipher

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def decrypt(text, key):
    return encrypt(text, -key)


if __name__ == "__main__":
    plaintext = input("Masukkan plaintext: ")
    key = int(input("Masukkan key (angka): "))

    ciphertext = encrypt(plaintext, key)
    print("Hasil Enkripsi:", ciphertext)

    decrypted = decrypt(ciphertext, key)
    print("Hasil Dekripsi:", decrypted)
```

---

## 6. Hasil dan Pembahasan

Program berhasil melakukan proses enkripsi dan dekripsi menggunakan algoritma Caesar Cipher. Pengguna dapat memasukkan teks dan nilai kunci berupa angka untuk menentukan besar pergeseran huruf.

Hasil eksekusi program Caesar Cipher:

![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)

Hasil yang diperoleh sesuai dengan teori Caesar Cipher, di mana setiap huruf bergeser sesuai nilai kunci. Jika terdapat karakter non-huruf, maka karakter tersebut tidak mengalami perubahan. Selama pengujian, tidak ditemukan error yang signifikan.

---

## 7. Jawaban Pertanyaan

* **Pertanyaan 1:** Apa kelemahan utama Caesar Cipher?
  **Jawaban:** Caesar Cipher mudah dipecahkan dengan brute force karena hanya memiliki jumlah kunci yang sangat terbatas.

* **Pertanyaan 2:** Mengapa Caesar Cipher tidak digunakan pada sistem keamanan modern?
  **Jawaban:** Karena tingkat keamanannya sangat rendah dan tidak mampu melindungi data dari serangan kriptografi modern.

---

## 8. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Caesar Cipher merupakan algoritma kriptografi klasik yang sederhana dan mudah dipahami. Praktikum ini membantu memahami konsep dasar enkripsi, dekripsi, dan penggunaan kunci dalam kriptografi.

---

## 9. Daftar Pustaka

* Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.
* Stallings, W. *Cryptography and Network Security*.

---

## 10. Commit Log

```
commit abc12345
Author: Muhammad Nizar Asagaf <muhammad.nizar@email.com>
Date:   2025-09-20

    praktikum-kriptografi: implementasi Caesar Cipher dan laporan praktikum
```
