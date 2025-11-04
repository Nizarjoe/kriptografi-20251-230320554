# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Implementasu Chipher Modern  
Nama: MUHAMMAD NIZAR ASAGAF  
NIM: 230320554  
Kelas: 5DSRA  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami dan mengimplementasikan algoritma kriptografi modern, yaitu DES (Data Encryption Standard), AES (Advanced Encryption Standard), dan RSA (Rivest–Shamir–Adleman).
Melalui praktikum ini mahasiswa diharapkan dapat:
Menerapkan proses enkripsi dan dekripsi menggunakan algoritma simetris (DES dan AES).
Mengimplementasikan algoritma asimetris RSA untuk mengenkripsi dan mendekripsi pesan.
Memahami perbedaan konsep keamanan antara cipher simetris dan asimetris.
Menjelaskan alasan mengapa algoritma modern digunakan sebagai standar keamanan pada sistem digital masa kini.

---

## 2. Dasar Teori
Kriptografi modern berperan penting dalam melindungi data dari akses tidak sah, terutama dalam komunikasi digital dan transaksi daring. Algoritma kriptografi modern dirancang untuk menahan serangan brute-force, analisis kriptografis, dan eksploitasi kelemahan struktural pada cipher klasik.

DES (Data Encryption Standard) merupakan algoritma blok cipher simetris yang dikembangkan pada tahun 1970-an oleh IBM dan disetujui oleh NIST sebagai standar enkripsi data. DES menggunakan kunci sepanjang 56 bit dengan blok data 64 bit. Walaupun dulu sangat populer, kini DES dianggap tidak aman karena kekuatan komputasi modern mampu menembusnya melalui serangan brute-force.

AES (Advanced Encryption Standard) adalah pengganti resmi DES yang diadopsi oleh NIST pada tahun 2001. AES bekerja dengan panjang kunci 128, 192, atau 256 bit dan ukuran blok tetap 128 bit. Keunggulan AES terletak pada kecepatannya, efisiensi struktur matematis, serta tingkat keamanan yang sangat tinggi, menjadikannya algoritma standar di hampir semua aplikasi keamanan modern seperti VPN, HTTPS, dan enkripsi perangkat penyimpanan.

RSA (Rivest–Shamir–Adleman) berbeda dari dua algoritma sebelumnya karena bersifat asimetris. Artinya, algoritma ini menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. RSA didasarkan pada kesulitan faktorisasi bilangan prima besar. Algoritma ini banyak digunakan dalam autentikasi, tanda tangan digital, dan pertukaran kunci pada protokol keamanan internet seperti SSL/TLS.

---

## 3. Alat dan Bahan
Python 3.11 atau versi lebih baru

Visual Studio Code / editor teks lain

Git dan akun GitHub untuk penyimpanan kode

Library pycryptodome sebagai pustaka kriptografi modern (pip install pycryptodome)

Perangkat komputer/laptop dengan sistem operasi Windows/Linux

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
Membuat folder proyek dengan struktur:

praktikum/week6-cipher-modern/
├─ src/
├─ screenshots/
└─ laporan.md


Menginstal library tambahan menggunakan perintah:

pip install pycryptodome


Membuat tiga file Python di dalam folder src/:

aes.py untuk implementasi AES-128

rsa.py untuk implementasi RSA

des.py (opsional) untuk simulasi DES

Menyalin dan menjalankan kode program sesuai panduan.

Menjalankan program satu per satu:

python src/aes.py
python src/rsa.py
python src/des.py


Melakukan screenshot hasil enkripsi dan dekripsi.

Menyimpan laporan dan hasil uji ke GitHub dengan commit message:

week6-cipher-modern

---

## 6. Hasil dan Pembahasan
a. AES (Advanced Encryption Standard)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt_decrypt():
    key = get_random_bytes(16)  # 128 bit
    cipher = AES.new(key, AES.MODE_EAX)

    plaintext = b"Modern Cipher AES Example"
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    print("=== AES Encryption ===")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)

    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted = cipher_dec.decrypt(ciphertext)
    print("Decrypted :", decrypted.decode())

if __name__ == "__main__":
    aes_encrypt_decrypt()

b. RSA (Rivest–Shamir–Adleman)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt_decrypt():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    plaintext = b"RSA Example"
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(plaintext)

    print("=== RSA Encryption ===")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)

    decipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted = decipher_rsa.decrypt(ciphertext)
    print("Decrypted :", decrypted.decode())

if __name__ == "__main__":
    rsa_encrypt_decrypt()

c. DES (Data Encryption Standard)
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_encrypt_decrypt():
    key = get_random_bytes(8)  # 64-bit key
    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = b"ABCDEFGH"
    ciphertext = cipher.encrypt(plaintext)

    print("=== DES Encryption ===")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)

    decipher = DES.new(key, DES.MODE_ECB)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted :", decrypted)

if __name__ == "__main__":
    des_encrypt_decrypt()


Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
DES dan AES sama-sama termasuk algoritma simetris, di mana satu kunci digunakan untuk enkripsi dan dekripsi. Namun, AES jauh lebih kuat karena panjang kunci lebih besar (128–256 bit) dan struktur transformasi datanya lebih kompleks. RSA adalah algoritma asimetris, artinya menggunakan dua kunci berbeda: public key untuk enkripsi dan private key untuk dekripsi. Dari sisi keamanan, RSA bergantung pada kesulitan faktorisasi bilangan prima besar, sementara AES bergantung pada transformasi blok nonlinier yang sulit dibalik tanpa kunci.

2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?
AES memiliki kecepatan tinggi, efisiensi tinggi, dan ketahanan terhadap berbagai jenis serangan kriptografis modern seperti differential cryptanalysis. Sementara DES sudah rentan karena ruang kunci yang kecil, memungkinkan serangan brute-force dilakukan dengan komputer modern hanya dalam hitungan jam. AES juga telah diadopsi sebagai standar global oleh NIST dan digunakan di berbagai protokol keamanan seperti HTTPS, Wi-Fi (WPA2/WPA3), dan VPN.

3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
RSA menggunakan dua kunci yang berbeda namun saling terkait secara matematis. Proses pembangkitan kuncinya melibatkan pemilihan dua bilangan prima besar (p dan q), menghitung hasil kali 
𝑛
=
𝑝
×
𝑞
n=p×q, serta menentukan nilai totient dan eksponen publik e. Kunci privat dihitung sebagai invers modular dari e terhadap totient. Karena proses ini melibatkan faktorisasi bilangan besar yang sangat sulit, RSA dianggap sangat aman, meskipun lambat dibanding algoritma simetris.

---

## 8. Kesimpulan
Praktikum ini membuktikan bahwa algoritma modern seperti AES dan RSA memberikan tingkat keamanan yang jauh lebih tinggi dibandingkan DES. AES unggul untuk enkripsi cepat dalam jumlah data besar, sedangkan RSA unggul dalam pertukaran kunci dan tanda tangan digital. DES tetap relevan hanya sebagai alat pembelajaran.
Dari hasil percobaan, proses enkripsi dan dekripsi berjalan sesuai teori dan menunjukkan bagaimana kunci kriptografi memengaruhi keamanan sistem secara signifikan.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit 9b3e4a1
Author: [Muhammad Nizar Asagaf] <joenizar470@gmail.com>
Date:   2025-11-04

    week6-cipher-modern: implementasi AES, RSA, dan laporan praktikum
```
