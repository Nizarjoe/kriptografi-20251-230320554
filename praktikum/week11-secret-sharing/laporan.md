Laporan Praktikum Kriptografi

Minggu ke-: 11
Topik: Shamir’s Secret Sharing (Secret Sharing)
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari praktikum ini adalah untuk memahami konsep Shamir’s Secret Sharing (SSS) sebagai metode pembagian rahasia ke beberapa pihak. Mahasiswa diharapkan mampu melakukan simulasi pembagian dan rekonstruksi rahasia, serta menganalisis tingkat keamanan skema secret sharing berbasis threshold.

2. Dasar Teori

Shamir’s Secret Sharing (SSS) merupakan skema kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (shares), sehingga rahasia tersebut hanya dapat direkonstruksi jika minimal sejumlah share tertentu (threshold) digabungkan. Skema ini diperkenalkan oleh Adi Shamir dan berbasis pada konsep interpolasi polinomial.

Dalam SSS, rahasia direpresentasikan sebagai konstanta dari sebuah polinomial berderajat k−1. Setiap share merupakan pasangan titik (x, y) yang dihasilkan dari evaluasi polinomial tersebut. Keamanan skema ini terletak pada fakta bahwa kurang dari k titik tidak cukup untuk merekonstruksi polinomial, sehingga rahasia tetap aman.

SSS banyak digunakan dalam sistem keamanan modern, seperti manajemen kunci kriptografi, sistem pemulihan data, dan pengamanan aset digital. Skema ini memberikan ketahanan terhadap kehilangan sebagian share dan kebocoran informasi parsial.

3. Alat dan Bahan

Python 3.11

Visual Studio Code

Git dan akun GitHub

Library Python:

secretsharing

4. Langkah Percobaan

Membuat folder praktikum/week11-secret-sharing/ sesuai struktur yang ditentukan.

Membuat file secret_sharing.py di dalam folder src/.

Menginstall library secretsharing menggunakan pip.

Menuliskan kode Python untuk membagi rahasia menggunakan Shamir Secret Sharing.

Melakukan rekonstruksi rahasia menggunakan sejumlah share sesuai threshold.

Menjalankan program dengan perintah:

python secret_sharing.py


Mengambil screenshot hasil pembagian dan rekonstruksi rahasia.

Menyusun laporan praktikum pada file laporan.md.

Melakukan commit ke repository Git dengan pesan week11-secret-sharing.

5. Source Code

Berikut adalah source code utama yang digunakan dalam praktikum ini:

from secretsharing import SecretSharer

# Rahasia yang akan dibagi
secret = "KriptografiUPB2025"

# Membagi rahasia menjadi 5 share dengan threshold 3
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:")
for share in shares:
    print(share)

# Rekonstruksi rahasia dari 3 share
recovered_secret = SecretSharer.recover_secret(shares[:3])
print("\nRecovered Secret:", recovered_secret)

6. Hasil dan Pembahasan

Program berhasil dijalankan dan menghasilkan lima buah share dari rahasia yang diberikan. Setiap share memiliki nilai unik dan tidak mengungkapkan rahasia secara langsung.

Rekonstruksi rahasia berhasil dilakukan menggunakan tiga share sesuai dengan nilai threshold yang ditentukan. Hal ini membuktikan bahwa skema Shamir Secret Sharing bekerja sesuai teori, di mana rahasia hanya dapat diperoleh jika jumlah share yang digunakan memenuhi ambang batas minimum.

Screenshot hasil pembagian dan rekonstruksi rahasia disimpan pada folder screenshots/ sebagai bukti keberhasilan praktikum.

7. Jawaban Pertanyaan

1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
Keuntungan utamanya adalah meningkatkan keamanan, karena tidak ada satu pihak pun yang memegang rahasia secara utuh. Rahasia hanya dapat direkonstruksi jika sejumlah share tertentu digabungkan.

2. Apa peran threshold (k) dalam keamanan secret sharing?
Threshold menentukan jumlah minimal share yang dibutuhkan untuk merekonstruksi rahasia. Nilai k menjaga keseimbangan antara keamanan dan ketersediaan data.

3. Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
SSS digunakan dalam manajemen kunci cryptocurrency, di mana kunci privat dompet dibagi ke beberapa pihak untuk mencegah kehilangan atau penyalahgunaan kunci oleh satu individu.

8. Kesimpulan

Praktikum ini menunjukkan bahwa Shamir’s Secret Sharing merupakan metode yang efektif untuk mendistribusikan rahasia secara aman. Dengan mekanisme threshold, skema ini memberikan perlindungan terhadap kebocoran sebagian data serta meningkatkan keandalan sistem keamanan.

9. Daftar Pustaka

Stinson, D. R. (2019). Cryptography: Theory and Practice. CRC Press.

Katz, J., & Lindell, Y. Introduction to Modern Cryptography.

10. Commit Log
commit abcdef987654
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-12-27

    week11-secret-sharing