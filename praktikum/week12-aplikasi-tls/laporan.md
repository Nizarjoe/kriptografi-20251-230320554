Laporan Praktikum Kriptografi

Minggu ke-: 12
Topik: Aplikasi TLS & E-commerce
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari praktikum ini adalah untuk menganalisis penerapan kriptografi pada SSL/TLS dalam layanan email dan website e-commerce. Mahasiswa juga diharapkan mampu memahami mekanisme enkripsi dalam transaksi online serta mengevaluasi isu etika dan privasi yang muncul dari penggunaan kriptografi dalam kehidupan sehari-hari.

2. Dasar Teori

Transport Layer Security (TLS) adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan internet. TLS merupakan pengembangan dari SSL (Secure Socket Layer) dan saat ini menjadi standar utama dalam komunikasi web yang aman, terutama pada protokol HTTPS.

Dalam sistem e-commerce, TLS digunakan untuk mengenkripsi data sensitif seperti username, password, dan informasi pembayaran. Proses ini memastikan kerahasiaan, integritas, dan autentikasi data antara klien dan server. Sertifikat digital yang dikeluarkan oleh Certificate Authority (CA) digunakan untuk memverifikasi identitas server.

Selain memberikan keamanan teknis, penggunaan kriptografi juga memunculkan tantangan etika dan privasi. Enkripsi melindungi hak privasi pengguna, namun di sisi lain dapat menimbulkan dilema dalam pengawasan, penegakan hukum, dan kebijakan perusahaan terhadap data komunikasi.

3. Alat dan Bahan

Browser (Google Chrome / Mozilla Firefox)

Koneksi internet

Git dan akun GitHub

Website e-commerce (Tokopedia, Shopee, dan sejenisnya)

4. Langkah Percobaan

Membuat folder praktikum/week12-aplikasi-tls/.

Mengakses website e-commerce menggunakan browser.

Mengecek sertifikat digital dengan mengklik ikon gembok (HTTPS).

Mencatat informasi sertifikat seperti issuer CA, masa berlaku, dan algoritma enkripsi.

Membandingkan akses website menggunakan HTTPS dan HTTP.

Mengambil screenshot informasi sertifikat digital.

Menyusun laporan hasil analisis pada file laporan.md.

Melakukan commit ke repository Git dengan pesan week12-aplikasi-tls.

5. Hasil Observasi

Berdasarkan hasil observasi pada dua website e-commerce, diperoleh informasi sebagai berikut:

Website 1: Tokopedia

Protokol: HTTPS

Issuer CA: DigiCert Inc

Masa berlaku: ± 1 tahun

Algoritma enkripsi: RSA dan AES

Website 2: Shopee

Protokol: HTTPS

Issuer CA: GlobalSign

Masa berlaku: ± 1 tahun

Algoritma enkripsi: RSA dan AES

Kedua website menggunakan TLS untuk melindungi komunikasi antara pengguna dan server.

Screenshot sertifikat digital disimpan pada folder screenshots/.

6. Pembahasan
A. Analisis TLS pada Web & Email

Website yang menggunakan HTTPS menunjukkan adanya enkripsi data selama proses komunikasi. Hal ini berbeda dengan HTTP yang mengirimkan data dalam bentuk plaintext sehingga mudah disadap. Pada layanan email, protokol seperti TLS digunakan untuk mengamankan komunikasi antar mail server.

B. Studi Kasus E-commerce

Pada transaksi e-commerce, TLS melindungi data login dan pembayaran dari serangan seperti Man-in-the-Middle (MITM). Tanpa TLS, penyerang dapat mencuri informasi sensitif pengguna, yang berpotensi menyebabkan pencurian identitas dan kerugian finansial.

C. Analisis Etika & Privasi

Penggunaan enkripsi pada email (PGP, S/MIME) menjaga privasi pengguna, namun menimbulkan dilema etika. Perusahaan terkadang ingin mengakses email karyawan untuk audit, sementara pengguna menuntut privasi. Selain itu, pemerintah menghadapi tantangan dalam penegakan hukum terhadap komunikasi terenkripsi tanpa melanggar hak privasi warga.

7. Jawaban Pertanyaan

1. Apa perbedaan utama antara HTTP dan HTTPS?
HTTP tidak menggunakan enkripsi, sedangkan HTTPS menggunakan TLS untuk mengenkripsi data sehingga komunikasi menjadi aman.

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
Sertifikat digital digunakan untuk memverifikasi identitas server dan mencegah pemalsuan identitas dalam komunikasi jaringan.

3. Bagaimana kriptografi mendukung privasi tetapi juga menimbulkan tantangan etika?
Kriptografi melindungi data dan privasi pengguna, namun dapat menyulitkan pengawasan hukum dan menimbulkan konflik antara keamanan, privasi, dan kepentingan institusi.

8. Kesimpulan

TLS merupakan teknologi penting dalam menjaga keamanan komunikasi digital, khususnya pada email dan e-commerce. Selain memberikan perlindungan teknis, penggunaan kriptografi juga harus mempertimbangkan aspek etika dan privasi agar keamanan tidak mengorbankan hak pengguna.

9. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security. Pearson Education.

Kahn Academy. TLS/SSL Overview.

10. Commit Log
commit abcdef121212
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-12-28

    week12-aplikasi-tls