Laporan Praktikum Kriptografi

Minggu ke-: 9
Topik: Digital Signature (RSA/DSA)
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: [Kelas]

1. Tujuan

Praktikum ini bertujuan untuk memberikan pemahaman mendalam tentang penerapan tanda tangan digital menggunakan algoritma RSA (Rivest–Shamir–Adleman) dan DSA (Digital Signature Algorithm).
Mahasiswa diharapkan mampu:
Mengimplementasikan proses pembuatan dan verifikasi tanda tangan digital.
Memahami bagaimana tanda tangan digital menjamin keaslian (authenticity) dan integritas (integrity) pesan.
Menyadari pentingnya tanda tangan digital dalam proses otentikasi data modern seperti dokumen elektronik, transaksi keuangan, dan komunikasi terenkripsi.

2. Dasar Teori

Tanda tangan digital merupakan teknik kriptografi yang digunakan untuk memastikan bahwa suatu pesan benar-benar dikirim oleh pihak yang berwenang dan tidak mengalami perubahan selama proses transmisi. Berbeda dengan tanda tangan manual, tanda tangan digital dihasilkan melalui proses matematis dengan memanfaatkan algoritma kriptografi kunci publik, seperti RSA atau DSA.
Dalam algoritma RSA, dua kunci digunakan: private key untuk menandatangani pesan, dan public key untuk memverifikasi tanda tangan. Prinsip dasarnya adalah bahwa hanya pemilik kunci privat yang bisa menghasilkan tanda tangan yang valid untuk suatu pesan tertentu, sedangkan siapa pun yang memiliki kunci publik dapat memverifikasi keasliannya.
Proses tanda tangan melibatkan hashing pesan terlebih dahulu menggunakan fungsi hash kriptografis (misalnya SHA-256), lalu hasil hash tersebut dienkripsi menggunakan kunci privat.
Sedangkan pada tahap verifikasi, penerima pesan akan melakukan proses hashing yang sama dan memverifikasi hasilnya menggunakan kunci publik pengirim.
Konsep ini memastikan dua hal utama:
Integritas – pesan tidak dapat diubah tanpa membuat tanda tangan menjadi tidak valid.
Autentikasi – hanya pemilik kunci privat yang dapat membuat tanda tangan yang valid.

3. Alat dan Bahan

Python 3.11 atau lebih baru
Visual Studio Code atau editor Python lain
Git dan akun GitHub untuk manajemen versi
Library tambahan:
pycryptodome untuk implementasi algoritma RSA, hashing, dan tanda tangan digital.

4. Langkah Percobaan

Membuat struktur folder:
praktikum/week9-digital-signature/
├─ src/
├─ screenshots/
└─ laporan.md
Menginstal library pycryptodome dengan perintah:
pip install pycryptodome
Membuat file src/signature.py.
Menulis kode Python untuk:
Membuat pasangan kunci RSA (private dan public key).
Menandatangani pesan dengan private key.
Memverifikasi tanda tangan dengan public key.
Menguji kasus modifikasi pesan untuk menunjukkan tanda tangan menjadi tidak valid.
Menjalankan program dengan perintah:
python src/signature.py
Mengambil screenshot hasil eksekusi dan menyimpannya di folder screenshots/.

5. Source Code
# src/signature.py

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan asli

message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key

signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

# Verifikasi tanda tangan dengan public key

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Uji modifikasi pesan

fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)
try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")

6. Hasil dan Pembahasan

Setelah menjalankan program, hasil yang ditampilkan di terminal menunjukkan bahwa tanda tangan digital berhasil diverifikasi pada pesan asli, dan gagal saat pesan diubah. Ini membuktikan bahwa tanda tangan digital sangat efektif dalam mendeteksi perubahan sekecil apa pun pada isi pesan.
Contoh hasil eksekusi:
Signature: 7f6a1b3d... (hexadecimal panjang)
Verifikasi berhasil: tanda tangan valid.
Verifikasi gagal: tanda tangan tidak cocok dengan pesan.
Tanda tangan digital mengandalkan kekuatan fungsi hash dan kriptografi kunci publik. Jika pesan diubah, nilai hash-nya berubah total, sehingga proses verifikasi otomatis gagal. Dalam konteks keamanan data, mekanisme ini mencegah serangan modifikasi atau manipulasi data di jaringan.
Hasil ini sesuai dengan teori yang menyebutkan bahwa hanya pemilik kunci privat yang dapat menghasilkan tanda tangan yang sah, sementara penerima hanya perlu memegang kunci publik untuk memverifikasi keaslian pesan.
Hasil eksekusi program RSA Digital Signature:

7. Jawaban Pertanyaan

1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan — penerima yang memiliki kunci privat dapat mendekripsi pesan terenkripsi. Sedangkan tanda tangan digital RSA berfungsi untuk otentikasi dan integritas pesan — pengirim menandatangani pesan dengan kunci privat, dan penerima memverifikasinya dengan kunci publik.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
Karena tanda tangan digital dibuat berdasarkan hash dari pesan, setiap perubahan sekecil apa pun akan mengubah nilai hash, sehingga tanda tangan menjadi tidak valid. Selain itu, hanya pemilik kunci privat yang dapat membuat tanda tangan yang sah, sehingga penerima dapat yakin terhadap identitas pengirim.

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
CA (Certificate Authority) berperan sebagai lembaga terpercaya yang menerbitkan sertifikat digital. Sertifikat ini berisi identitas pemilik kunci publik dan menjamin bahwa kunci publik tersebut benar-benar milik individu atau organisasi yang sah. Tanpa CA, sulit untuk membedakan antara kunci publik asli dan palsu di dunia nyata.

8. Kesimpulan

Dari praktikum ini dapat disimpulkan bahwa tanda tangan digital menggunakan algoritma RSA mampu menjamin keaslian dan integritas pesan. Proses verifikasi berhasil jika pesan asli tidak diubah, dan gagal ketika pesan dimodifikasi. Dengan demikian, mekanisme ini menjadi pondasi penting dalam keamanan komunikasi digital modern seperti transaksi online, dokumen hukum, dan email terenkripsi.

9. Daftar Pustaka

Stinson, D. R., & Paterson, M. B. (2019). Cryptography: Theory and Practice. CRC Press.
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.
Katz, J., & Lindell, Y. (2021). Introduction to Modern Cryptography. CRC Press.

10. Commit Log
commit 4a9f2e7
Author: [Nama Mahasiswa] <[email]>
Date:   2025-11-11

    week9-digital-signature: implementasi tanda tangan digital RSA dan laporan praktikum