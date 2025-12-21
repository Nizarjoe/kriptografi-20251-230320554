Laporan Praktikum Kriptografi

Minggu ke-: 14
Topik: Analisis Serangan Kriptografi
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari praktikum ini adalah untuk mengidentifikasi jenis serangan kriptografi pada sistem nyata, mengevaluasi kelemahan algoritma atau implementasi yang digunakan, serta memberikan rekomendasi solusi kriptografi yang lebih aman untuk meningkatkan keamanan sistem.

2. Dasar Teori

Serangan kriptografi merupakan upaya untuk mengeksploitasi kelemahan pada algoritma kriptografi, implementasi, atau konfigurasi sistem keamanan. Serangan ini dapat berupa brute force, dictionary attack, Man-in-the-Middle (MITM), replay attack, maupun eksploitasi algoritma hash yang sudah tidak aman.

Banyak sistem lama masih menggunakan algoritma kriptografi yang telah terbukti lemah, seperti MD5 atau SHA-1, karena alasan kompatibilitas dan kurangnya pembaruan sistem. Selain itu, kesalahan implementasi dan konfigurasi yang tidak tepat juga menjadi faktor utama terjadinya serangan.

Analisis serangan kriptografi penting dilakukan untuk memastikan bahwa sistem informasi tetap aman terhadap ancaman yang terus berkembang, serta untuk menentukan algoritma dan mekanisme keamanan yang sesuai dengan standar terkini.

3. Alat dan Bahan

Browser dan koneksi internet

Git dan akun GitHub

Dokumentasi algoritma kriptografi

Contoh hash atau skenario serangan (studi kasus)

4. Studi Kasus Serangan
A. Identifikasi Serangan

Studi kasus yang dianalisis adalah serangan brute force dan dictionary attack pada password yang disimpan menggunakan hash MD5. MD5 merupakan algoritma hash lama yang sudah tidak aman dan rentan terhadap collision serta serangan brute force menggunakan rainbow table.

Vektor serangan terjadi ketika database password bocor dan penyerang dapat dengan mudah memecahkan hash MD5 menggunakan tool otomatis.

5. Evaluasi Kelemahan

Kelemahan utama pada kasus ini terletak pada algoritma kriptografi yang digunakan, yaitu MD5. Algoritma ini tidak dirancang untuk perlindungan password karena:

Proses hashing sangat cepat sehingga mudah di-brute force.

Tidak menggunakan salt secara default.

Sudah banyak database hash MD5 yang tersedia secara publik.

Selain algoritma, kelemahan juga muncul dari sisi implementasi, yaitu tidak diterapkannya mekanisme pengamanan tambahan seperti salting dan key stretching.

6. Rekomendasi Solusi

Untuk meningkatkan keamanan sistem, berikut rekomendasi yang diberikan:

Mengganti algoritma hash MD5 dengan algoritma yang lebih aman seperti bcrypt, scrypt, atau Argon2.

Menggunakan salt unik untuk setiap password guna mencegah rainbow table attack.

Menerapkan kebijakan password yang kuat (panjang minimal, kombinasi karakter).

Melakukan audit dan pembaruan sistem keamanan secara berkala.

Penerapan solusi ini dapat meningkatkan ketahanan sistem terhadap brute force dan serangan dictionary secara signifikan.

7. Hasil dan Pembahasan

Hasil analisis menunjukkan bahwa penggunaan algoritma kriptografi yang sudah usang merupakan risiko besar bagi keamanan sistem. Dengan mengganti algoritma hash dan memperbaiki implementasi, sistem dapat terlindungi lebih baik dari serangan yang umum terjadi.

Screenshot ilustrasi hash lemah atau simulasi brute force disimpan pada folder screenshots/ sebagai bukti pendukung analisis.

8. Jawaban Pertanyaan Diskusi

1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Karena masih menggunakan algoritma kriptografi lama, kebijakan password lemah, serta kurangnya pembaruan dan audit keamanan.

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan algoritma berasal dari desain kriptografinya, sedangkan kelemahan implementasi berasal dari cara algoritma tersebut diterapkan dalam sistem.

3. Bagaimana organisasi dapat memastikan sistem kriptografi tetap aman di masa depan?
Dengan menerapkan standar kriptografi terbaru, melakukan update rutin, audit keamanan berkala, dan mengikuti rekomendasi komunitas keamanan.

9. Kesimpulan

Berdasarkan praktikum ini, dapat disimpulkan bahwa analisis serangan kriptografi sangat penting untuk mengidentifikasi risiko keamanan sistem. Penggunaan algoritma yang tepat dan implementasi yang benar dapat secara signifikan meningkatkan perlindungan terhadap serangan siber.

10. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security. Pearson Education.

Stinson, D. R. (2019). Cryptography: Theory and Practice. CRC Press.

11. Commit Log
commit abcdef141414
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-01-10

    week14-analisis-serangan
