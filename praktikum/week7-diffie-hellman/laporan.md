Laporan Praktikum Kriptografi

Minggu ke-: 7
Topik: Diffie-Hellman Key Exchange
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5DSRA

1. Tujuan

Praktikum ini bertujuan agar mahasiswa memahami dan mampu menerapkan konsep dasar dari algoritma Diffie-Hellman Key Exchange, salah satu pondasi utama dalam sistem kriptografi modern. Secara khusus, mahasiswa diharapkan dapat:

Melakukan simulasi proses pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.

Menjelaskan bagaimana dua pihak dapat saling berbagi kunci secara aman melalui saluran publik tanpa membocorkan rahasianya.

Mengidentifikasi serta menganalisis potensi kelemahan protokol Diffie-Hellman, terutama terhadap serangan Man-in-the-Middle (MITM) yang dapat mengancam integritas komunikasi digital.

2. Dasar Teori

Diffie-Hellman Key Exchange (DHKE) diperkenalkan pada tahun 1976 oleh Whitfield Diffie dan Martin Hellman sebagai metode pertama yang memungkinkan dua pihak untuk membentuk kunci rahasia bersama tanpa perlu bertemu langsung. Ide utama dari algoritma ini adalah memanfaatkan sifat matematika dari operasi eksponensial dalam modulo bilangan prima besar, di mana menghitung perpangkatan relatif mudah, tetapi menghitung logaritma diskrit (mencari pangkatnya) sangat sulit.

Proses pertukaran kunci dilakukan melalui beberapa tahap: kedua pihak terlebih dahulu menyepakati dua parameter publik, yaitu bilangan prima besar p dan bilangan basis (generator) g. Masing-masing pihak kemudian memilih kunci privat secara acak, menghitung kunci publiknya dengan rumus A = g^a mod p dan B = g^b mod p, lalu menukarkannya secara terbuka. Dengan menghitung B^a mod p dan A^b mod p, keduanya akan memperoleh nilai yang sama, yaitu shared secret key.

Namun, Diffie-Hellman murni tidak menyediakan autentikasi. Artinya, tidak ada jaminan bahwa pihak yang berkomunikasi adalah benar-benar pihak yang dimaksud. Hal ini memungkinkan munculnya serangan MITM, di mana penyerang (Eve) dapat menyisipkan dirinya di antara komunikasi Alice dan Bob, mengganti nilai publik, lalu membentuk dua kunci rahasia terpisah dengan masing-masing pihak. Akibatnya, komunikasi terenkripsi tetap dapat dibaca oleh Eve tanpa diketahui korban.

3. Alat dan Bahan

Python 3.x sebagai bahasa pemrograman utama.

Visual Studio Code atau editor teks lain untuk menulis dan menjalankan kode.

Git dan akun GitHub untuk dokumentasi versi dan bukti commit.

Terminal / Command Prompt untuk mengeksekusi program.

Folder praktikum dengan struktur sesuai panduan:

praktikum/week7-diffie-hellman/
├─ src/
├─ screenshots/
└─ laporan.md

4. Langkah Percobaan

Membuat struktur folder seperti di atas.

Membuat file baru bernama diffie_hellman.py di dalam folder src/.

Menulis kode Python untuk melakukan simulasi proses pertukaran kunci Diffie-Hellman.

Menjalankan program untuk memastikan hasil kunci rahasia yang diperoleh oleh kedua pihak sama.

Menambahkan simulasi sederhana untuk menunjukkan skenario MITM.

Mengambil tangkapan layar hasil program dan menyimpannya di folder screenshots/.

Melakukan commit dengan pesan week7-diffie-hellman.

5. Source Code
import random

# parameter publik
p = 23  # bilangan prima
g = 5   # generator

# kunci privat Alice dan Bob
a = random.randint(1, p-1)
b = random.randint(1, p-1)

# kunci publik
A = pow(g, a, p)
B = pow(g, b, p)

# pertukaran kunci publik
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Nilai p (prima):", p)
print("Nilai g (generator):", g)
print("Kunci privat Alice:", a)
print("Kunci publik Alice:", A)
print("Kunci privat Bob:", b)
print("Kunci publik Bob:", B)
print("Kunci bersama Alice:", shared_secret_A)
print("Kunci bersama Bob:", shared_secret_B)

6. Hasil dan Pembahasan

Hasil percobaan menunjukkan bahwa nilai kunci bersama yang dihasilkan oleh Alice (shared_secret_A) dan Bob (shared_secret_B) identik, menandakan bahwa proses pertukaran kunci berhasil. Hal ini membuktikan efektivitas metode Diffie-Hellman dalam membangun kunci rahasia bersama melalui saluran publik.

Contoh hasil eksekusi program:

Nilai p (prima): 23
Nilai g (generator): 5
Kunci privat Alice: 6
Kunci publik Alice: 8
Kunci privat Bob: 15
Kunci publik Bob: 19
Kunci bersama Alice: 2
Kunci bersama Bob: 2


Kedua pihak memperoleh kunci rahasia bersama sebesar 2, meskipun mereka tidak pernah membagikan kunci privatnya secara langsung. Ini menjadi bukti nyata bahwa keamanan terjaga selama pihak ketiga tidak dapat menghitung logaritma diskrit dari nilai publik yang dikirimkan.

Pada tahap berikutnya dilakukan simulasi serangan MITM. Pihak ketiga (Eve) mencegat nilai publik yang dikirim Alice dan Bob, lalu menggantinya dengan miliknya. Hasilnya, Alice dan Bob tidak lagi memiliki kunci rahasia yang sama, sementara Eve berhasil mengetahui kedua kunci tersebut. Fenomena ini menggambarkan ancaman nyata dari protokol Diffie-Hellman jika digunakan tanpa autentikasi tambahan.

Hasil eksekusi program:


7. Jawaban Pertanyaan

1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Diffie-Hellman dirancang berdasarkan konsep matematika yang sulit dipecahkan, yaitu masalah logaritma diskrit. Meskipun nilai publik seperti p, g, A, dan B diketahui semua orang, kunci rahasia (a dan b) tetap tidak dapat dihitung tanpa melakukan perhitungan logaritma diskrit yang secara komputasi sangat sulit, terutama jika p adalah bilangan prima besar. Inilah yang membuat Diffie-Hellman aman digunakan pada saluran terbuka seperti internet. Dengan hanya bertukar nilai publik, kedua pihak dapat menghasilkan shared secret key yang identik tanpa pernah mengirimkan kunci rahasia mereka.

2. Apa kelemahan utama protokol Diffie-Hellman murni?
Kelemahan utamanya adalah tidak adanya autentikasi identitas. Protokol ini tidak dapat memastikan bahwa pihak yang diajak bertukar kunci benar-benar pihak yang dimaksud. Hal ini memungkinkan munculnya Man-in-the-Middle Attack, di mana penyerang dapat menyamar sebagai lawan bicara, mengintersep komunikasi, lalu membentuk dua sesi pertukaran kunci yang berbeda. Selain itu, Diffie-Hellman juga rentan terhadap serangan replay atau penggunaan parameter publik yang lemah, seperti bilangan prima kecil yang dapat diprediksi.

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
Untuk mencegah serangan MITM, protokol Diffie-Hellman harus dikombinasikan dengan mekanisme autentikasi. Beberapa pendekatan yang umum digunakan antara lain:

Mengintegrasikan sertifikat digital (X.509) untuk memverifikasi identitas pihak yang berkomunikasi.

Menggunakan tanda tangan digital pada nilai publik yang ditukar agar pihak lain dapat memastikan keasliannya.

Mengimplementasikan Diffie-Hellman di atas protokol aman seperti TLS (Transport Layer Security) yang sudah memiliki lapisan autentikasi.
Dengan langkah-langkah tersebut, komunikasi menjadi lebih aman karena setiap nilai publik dapat diverifikasi asal-usulnya sebelum digunakan untuk pembentukan kunci rahasia bersama.

8. Kesimpulan

Praktikum ini menunjukkan bahwa algoritma Diffie-Hellman adalah metode yang efektif untuk membentuk kunci rahasia bersama melalui saluran publik. Prinsip keamanannya bertumpu pada kesulitan matematis dalam menyelesaikan logaritma diskrit. Hasil simulasi membuktikan bahwa kedua pihak dapat memperoleh kunci yang sama tanpa bertukar kunci privat.

Namun, dari hasil analisis juga terlihat bahwa versi dasar Diffie-Hellman tidak cukup aman terhadap serangan MITM. Oleh karena itu, penggunaan mekanisme autentikasi tambahan seperti tanda tangan digital atau sertifikat sangat penting untuk memastikan keaslian komunikasi dan mencegah penyusupan pihak ketiga.

9. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson Education.

Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography. CRC Press.

Schneier, B. (2015). Applied Cryptography: Protocols, Algorithms, and Source Code in C. Wiley.

10. Commit Log
commit 7df4b12c
Author: [Muhammad Nizar Asagaf] <[joenizar470@gmail.com]>
Date:   2025-11-11

    week7-diffie-hellman: implementasi simulasi Diffie-Hellman dan analisis serangan MITM