Laporan Praktikum Kriptografi

Minggu ke-: 3
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Menyelesaikan operasi aritmetika modular menggunakan Python.

Menghitung GCD menggunakan algoritma Euclidean.

Menentukan invers modular dengan algoritma Euclidean lanjutan.

Mensimulasikan logaritma diskrit sederhana sebagai dasar kriptografi modern.

2. Dasar Teori

Aritmetika modular merupakan sistem perhitungan dengan batas nilai tertentu (modulus) di mana hasil operasi dikembalikan sebagai sisa pembagian. Operasi ini menjadi dasar berbagai algoritma kriptografi modern seperti RSA dan Diffie-Hellman.

GCD (Greatest Common Divisor) adalah bilangan terbesar yang dapat membagi dua bilangan tanpa sisa. Algoritma Euclidean digunakan untuk menghitung GCD secara efisien. Versi lanjutan dari algoritma ini, yaitu Extended Euclidean Algorithm, digunakan untuk mencari modular inverse.

Logaritma diskrit adalah masalah mencari nilai eksponen x dalam persamaan a^x ≡ b (mod n). Masalah ini sulit diselesaikan jika n besar, sehingga digunakan dalam sistem keamanan berbasis kriptografi kunci publik.

3. Alat dan Bahan

Python 3.11 atau lebih baru

Visual Studio Code

Git dan akun GitHub

Sistem operasi Windows / Linux

Library bawaan Python (tidak memerlukan eksternal)

4. Langkah Percobaan

Membuat folder praktikum/week3-modmath-gcd/ dengan struktur:

├─ src/
├─ screenshots/
└─ laporan.md


Membuat file src/modular_math.py.

Menyalin kode dari panduan praktikum ke dalam file tersebut.

Menjalankan program dengan perintah:

python src/modular_math.py


Melakukan screenshot hasil eksekusi dan menyimpannya di screenshots/hasil.png.

Melakukan commit ke repository GitHub dengan pesan:

week3-modmath-gcd

5. Source Code
# ============================================
# Modular Math, GCD, dan Discrete Logarithm
# Week 3 - Praktikum Kriptografi Dasar
# ============================================

# ---- Aritmetika Modular ----
def mod_add(a, b, n): 
    return (a + b) % n

def mod_sub(a, b, n): 
    return (a - b) % n

def mod_mul(a, b, n): 
    return (a * b) % n

def mod_exp(base, exp, n): 
    return pow(base, exp, n)

# ---- Algoritma Euclidean ----
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# ---- Extended Euclidean Algorithm ----
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

# ---- Logaritma Diskrit ----
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

# ---- Uji Program ----
if __name__ == "__main__":
    print("=== Aritmetika Modular ===")
    print("7 + 5 mod 12 =", mod_add(7, 5, 12))
    print("7 - 5 mod 12 =", mod_sub(7, 5, 12))
    print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
    print("7^128 mod 13 =", mod_exp(7, 128, 13))

    print("\n=== GCD & Euclidean Algorithm ===")
    print("gcd(54, 24) =", gcd(54, 24))

    print("\n=== Extended Euclidean & Invers Modular ===")
    print("Invers 3 mod 11 =", modinv(3, 11))

    print("\n=== Logaritma Diskrit ===")
    print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))

6. Hasil dan Pembahasan

Hasil eksekusi program menunjukkan bahwa seluruh fungsi berjalan sesuai teori.
Berikut hasil keluaran di terminal:

=== Aritmetika Modular ===
7 + 5 mod 12 = 0
7 - 5 mod 12 = 2
7 * 5 mod 12 = 11
7^128 mod 13 = 9

=== GCD & Euclidean Algorithm ===
gcd(54, 24) = 6

=== Extended Euclidean & Invers Modular ===
Invers 3 mod 11 = 4

=== Logaritma Diskrit ===
3^x ≡ 4 (mod 7), x = 4


Semua hasil sesuai ekspektasi. Tidak ditemukan error selama percobaan.

Hasil eksekusi program:

7. Jawaban Pertanyaan

Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular digunakan untuk menjaga semua operasi dalam ruang terbatas, yang menjadi dasar sistem enkripsi seperti RSA dan ECC.

Mengapa invers modular penting dalam algoritma kunci publik (RSA)?
Invers modular digunakan untuk menentukan kunci privat (d), di mana d merupakan invers dari e (mod φ(n)).

Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
Karena tidak ada algoritma efisien, penyelesaiannya menjadi sulit dan memerlukan waktu eksponensial, sehingga digunakan untuk menjamin keamanan sistem kriptografi modern.

8. Kesimpulan

Pada praktikum ini, mahasiswa telah berhasil menerapkan operasi aritmetika modular, algoritma Euclidean, dan logaritma diskrit menggunakan Python.
Konsep-konsep ini menjadi dasar penting bagi algoritma kriptografi modern yang menggunakan operasi bilangan besar secara modular.

9. Daftar Pustaka

Katz, J., & Lindell, Y. (2020). Introduction to Modern Cryptography.

Stallings, W. (2017). Cryptography and Network Security: Principles and Practice.

Dokumentasi resmi Python: https://docs.python.org/3/library/functions.html#pow

10. Commit Log
commit 7f3a21b
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-10-28

    week3-modmath-gcd: implementasi modular arithmetic, GCD, invers modular, dan logaritma diskrit
