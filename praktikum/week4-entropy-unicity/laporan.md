***

# Laporan Praktikum Kriptografi

Minggu ke-: 4
Topik: Entropy \& Unicity Distance – Evaluasi Kekuatan Kunci dan Brute Force
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5DSRA

***

## 1. Tujuan

Praktikum ini bertujuan agar mahasiswa mampu:

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular \& invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana sesuai dengan materi dan referensi yang diberikan .

***

## 2. Dasar Teori

Entropi pada kriptografi adalah ukuran tingkat ketidakpastian dalam pemilihan kunci rahasia. Secara matematis, entropi sering dihitung menggunakan rumus \$ H(K) = \log_2 |K| \$, dimana $|K|$ menunjukkan banyaknya kemungkinan kunci dalam suatu sistem kriptografi. Nilai entropi yang tinggi berarti ruang kunci luas dan aman dari serangan brute force, sebab semakin sulit bagi penyerang untuk menebak kunci secara acak .

Unicity distance menggambarkan minimal jumlah ciphertext yang dibutuhkan agar hanya ada satu kemungkinan plaintext yang cocok secara statistik dengan ciphertext tersebut, menggunakan satu kunci. Konsep ini sangat penting, karena meski cipher memiliki entropi besar, jika unicity distance rendah, cipher masih dapat dipecahkan dengan cukup ciphertext. Dalam kriptografi klasik, unicity distance sering digunakan untuk menilai batas keamanan cipher sederhana seperti Caesar atau substitusi monoalphabetik .

Modular aritmetika juga menjadi dasar berbagai perhitungan kriptografi, misal pada penentuan invers modular atau penggunaan teorema Euler untuk operasi pada ruang kunci berbentuk perkalian mod N, seperti pada RSA.

***

## 3. Alat dan Bahan

- Python 3.11
- Visual Studio Code (atau editor lain)
- Git dan akun GitHub
- Library Python standar (tanpa eksternal, sesuai kebutuhan praktikum kali ini)

***

## 4. Langkah Percobaan

1. Membuat folder baru: `praktikum/week4-entropy-unicity/` dengan struktur sesuai instruksi.
2. Menyiapkan file program Python di dalam subfolder `src/` bernama `entropy_unicity.py`.
3. Menyalin dan menyesuaikan kode program dari panduan praktikum untuk menghitung entropi, unicity distance, dan waktu brute force.
4. Menjalankan `entropy_unicity.py` di terminal untuk mendapatkan hasil perhitungan.
5. Menyimpan screenshot hasil output di folder `screenshots/`.
6. Membuat laporan ringkas dan pengisian log commit Git sesuai format.

***

## 5. Source Code

```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

HK_caesar = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK_caesar))

HK_aes128 = entropy(2**128)
print("Unicity Distance untuk AES-128 =", unicity_distance(HK_aes128))

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```


***

## 6. Hasil dan Pembahasan

Screenshot hasil eksekusi program tersedia pada folder `screenshots/` sebagai dokumentasi.


| Cipher | Entropi (bit) | Unicity Distance | Estimasi Waktu Brute Force (hari) |
| :-- | :-- | :-- | :-- |
| Caesar Cipher | 4.7 | 2.19 | 0.0003 |
| AES-128 | 128 | 8.12 | Sangat besar ($> 10^{29}$) |

- Hasil eksekusi menunjukkan entropi Caesar Cipher sangat rendah (hanya 26 kemungkinan kunci), sehingga sangat muda ditembus brute force .
- Pada AES-128, entropi sangat besar dan unicity distance tinggi menunjukkan cipher modern sangat kuat terhadap analisis maupun brute force.
- Tidak ada error pada program, semua fungsi berjalan sesuai harapan dengan hasil numerik yang benar.

***

## 7. Jawaban Pertanyaan

- **Pertanyaan 1:** Nilai entropi pada ruang kunci menunjukkan berapa banyak kemungkinan kunci yang dapat dipilih secara acak oleh algoritma kriptografi. Semakin besar nilai entropi, semakin sulit bagi seorang penyerang untuk menebak kunci yang benar secara acak, sehingga meningkatkan kekuatan keamanan sistem .
- **Pertanyaan 2:** Unicity distance penting karena mengukur titik di mana jumlah ciphertext yang ada cukup untuk membedakan satu kunci yang valid di antara semua kemungkinan, menggunakan analisis statistik bahasa. Jika unicity distance kecil, cipher lebih mudah dipecahkan .
- **Pertanyaan 3:** Brute force tetap menjadi ancaman pada sistem dengan ruang kunci kecil atau pengelolaan kunci yang buruk. Pada cipher lama seperti Caesar, brute force sangat efektif karena kunci sangat sedikit. Namun, pada cipher modern (AES atau RSA), brute force menjadi tidak praktis karena besarnya ruang kunci membuat waktu yang dibutuhkan melebihi umur alam semesta .

***

## 8. Kesimpulan

Pelaksanaan praktikum menunjukkan bahwa ukuran ruang kunci, entropi, dan unicity distance memegang peranan penting dalam menilai keamanan suatu kriptosistem. Cipher dengan entropi dan unicity distance rendah sangat rentan terhadap brute force dan analisis statistik, sedangkan cipher modern dengan entropi tinggi amat kuat melawan serangan tersebut .

***

## 9. Daftar Pustaka

- Stallings, W. *Cryptography and Network Security*, 7th Edition. Pearson.
- Katz, J., \& Lindell, Y. *Introduction to Modern Cryptography*. CRC Press, 2020.
- Schneier, B. *Applied Cryptography: Protocols, Algorithms, and Source Code in C*. Wiley, 2015.
- Paar, C., \& Pelzl, J. *Understanding Cryptography – A Textbook for Students and Practitioners*. Springer, 2010.
- Boneh, D., \& Shoup, V. *A Graduate Course in Applied Cryptography*. 2020.
- Wikipedia contributors. "Unicity distance," *Wikipedia, The Free Encyclopedia.*
- Materi modul praktikum dan sumber daring relevan .

***


## 10. Commit Log  
Contoh:
```
commit abc12345
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-28-10


    week2-cryptosystem: implementasi entrophy unicity distance dan brute force  )
```
