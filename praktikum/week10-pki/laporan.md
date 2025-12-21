Laporan Praktikum Kriptografi

Minggu ke-: 10
Topik: Public Key Infrastructure (PKI) & Certificate Authority
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari praktikum ini adalah untuk memahami konsep Public Key Infrastructure (PKI) dan peran Certificate Authority (CA) dalam sistem keamanan komunikasi. Mahasiswa diharapkan mampu membuat sertifikat digital sederhana, memahami proses verifikasi sertifikat, serta menganalisis pentingnya PKI dalam komunikasi aman seperti HTTPS dan TLS.

2. Dasar Teori

Public Key Infrastructure (PKI) merupakan sistem yang digunakan untuk mengelola kunci publik dan sertifikat digital dalam rangka menjamin keamanan komunikasi. PKI bekerja dengan memanfaatkan kriptografi kunci publik, di mana setiap entitas memiliki sepasang kunci, yaitu kunci publik dan kunci privat. Sertifikat digital digunakan untuk mengaitkan identitas pemilik dengan kunci publik secara sah.

Certificate Authority (CA) adalah pihak ketiga yang tepercaya yang bertugas menerbitkan, menandatangani, dan memverifikasi sertifikat digital. Dalam implementasi nyata, browser dan sistem operasi menyimpan daftar CA tepercaya untuk memastikan bahwa sertifikat HTTPS yang digunakan server adalah valid dan dapat dipercaya.

PKI berperan penting dalam mencegah serangan seperti Man-in-the-Middle (MITM). Dengan adanya verifikasi sertifikat, klien dapat memastikan bahwa komunikasi dilakukan dengan pihak yang sah, sehingga data yang dikirim tetap aman dan terenkripsi.

3. Alat dan Bahan

Python 3.11

Visual Studio Code

Git dan akun GitHub

Library Python:

cryptography

pyopenssl

4. Langkah Percobaan

Membuat folder praktikum/week10-pki/ sesuai struktur yang ditentukan.

Membuat file pki_cert.py di dalam folder src/.

Menuliskan kode Python untuk menghasilkan pasangan kunci RSA.

Membuat sertifikat digital self-signed menggunakan library cryptography.

Menyimpan sertifikat dalam format .pem.

Menjalankan program dengan perintah:

python pki_cert.py


Mengambil screenshot hasil eksekusi program.

Menyusun laporan praktikum pada file laporan.md.

Melakukan commit ke repository Git dengan pesan week10-pki.

5. Source Code

Berikut adalah source code utama yang digunakan dalam praktikum ini:

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Subject dan issuer (self-signed certificate)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Membuat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Menyimpan sertifikat ke file
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")

6. Hasil dan Pembahasan

Program berhasil dijalankan tanpa error dan menghasilkan file sertifikat digital bernama cert.pem. Sertifikat tersebut merupakan self-signed certificate, di mana subject dan issuer memiliki identitas yang sama.

File sertifikat tersimpan dalam format PEM dan dapat dibuka menggunakan text editor atau diverifikasi menggunakan OpenSSL. Hasil ini sesuai dengan tujuan praktikum, yaitu membuat sertifikat digital sederhana sebagai simulasi PKI.

Screenshot hasil eksekusi program disimpan pada folder screenshots/ sebagai bukti keberhasilan praktikum.

7. Jawaban Pertanyaan

1. Apa fungsi utama Certificate Authority (CA)?
Certificate Authority berfungsi sebagai pihak tepercaya yang menerbitkan dan menandatangani sertifikat digital untuk menjamin keaslian identitas pemilik sertifikat.

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Karena sertifikat self-signed tidak diverifikasi oleh CA tepercaya, sehingga browser dan klien tidak dapat memastikan keaslian identitas server dan berpotensi menimbulkan risiko keamanan.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan MITM dengan memastikan bahwa kunci publik server telah diverifikasi oleh CA, sehingga klien dapat memastikan komunikasi dilakukan dengan pihak yang sah.

8. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa PKI merupakan komponen penting dalam sistem keamanan komunikasi modern. Sertifikat digital dan peran CA memungkinkan proses autentikasi yang aman serta melindungi data dari serangan pihak tidak bertanggung jawab.

9. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security. Pearson Education.

Katz, J., & Lindell, Y. Introduction to Modern Cryptography.

10. Commit Log
commit abcdef123456
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-12-20

    week10-pki