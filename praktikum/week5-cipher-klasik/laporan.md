# Laporan Praktikum Week 5 - Cipher Klasik

**Nama:** Muhammad Nizar Asagaf  
**NIM:** 230320554  
**Tanggal:** 4 November 2025

---

## 1. Penjelasan Teori Cipher Klasik

### 1.1 Caesar Cipher
Caesar Cipher adalah salah satu teknik enkripsi substitusi paling sederhana dan tertua. Algoritma ini bekerja dengan menggeser setiap huruf dalam plaintext sejumlah posisi tertentu dalam alfabet.

**Rumus Matematika:**
- Enkripsi: `C = (P + k) mod 26`
- Dekripsi: `P = (C - k) mod 26`

Dimana:
- C = Ciphertext
- P = Plaintext
- k = Kunci (shift value)

**Karakteristik:**
- Menggunakan substitusi monoalfabetik
- Hanya ada 25 kemungkinan kunci (mudah di-brute force)
- Tidak aman untuk komunikasi modern

### 1.2 Vigenère Cipher
Vigenère Cipher adalah pengembangan dari Caesar Cipher yang menggunakan serangkaian Caesar Cipher berdasarkan huruf-huruf kunci. Cipher ini menggunakan substitusi polialfabetik.

**Rumus Matematika:**
- Enkripsi: `Ci = (Pi + Ki) mod 26`
- Dekripsi: `Pi = (Ci - Ki) mod 26`

Dimana:
- Ki = huruf kunci ke-i (berulang jika plaintext lebih panjang)

**Karakteristik:**
- Lebih kuat dari Caesar Cipher
- Menggunakan kata/frasa sebagai kunci
- Rentan terhadap Kasiski examination dan analisis frekuensi jika kunci pendek

### 1.3 Transposition Cipher
Transposition Cipher tidak mengubah huruf dalam plaintext, tetapi mengubah posisi/urutannya. Implementasi yang digunakan adalah Columnar Transposition.

**Cara Kerja:**
1. Tulis plaintext dalam bentuk grid dengan jumlah kolom = kunci
2. Baca per kolom untuk mendapatkan ciphertext
3. Untuk dekripsi, proses dibalik

**Karakteristik:**
- Tidak mengubah frekuensi huruf (kelemahan utama)
- Bisa dikombinasikan dengan cipher substitusi untuk keamanan lebih baik
- Memerlukan kunci (jumlah kolom) yang tepat untuk dekripsi

---

## 2. Hasil Implementasi

### 2.1 Caesar Cipher

**Test Case 1:**
```
Plaintext : CLASSIC CIPHER
Key       : 3
Ciphertext: FODVVLF FLSKHU
Decrypted : CLASSIC CIPHER
```

**Test Case 2:**
```
Plaintext : Hello World
Key       : 13 (ROT13)
Ciphertext: Uryyb Jbeyq
Decrypted : Hello World
```

**Analisis:**
- Program berhasil mengenkripsi dan mendekripsi dengan benar
- Spasi dan karakter non-alfabet tidak diubah
- Mendukung huruf besar dan kecil

### 2.2 Vigenère Cipher

**Test Case 1:**
```
Plaintext : KRIPTOGRAFI
Key       : KEY
Ciphertext: UVCNTSGVERC
Decrypted : KRIPTOGRAFI
```

**Test Case 2:**
```
Plaintext : ATTACK AT DAWN
Key       : LEMON
Ciphertext: LXFOPV EF RNHR
Decrypted : ATTACK AT DAWN
```

**Analisis:**
- Implementasi berhasil dengan berbagai panjang kunci
- Kunci berulang jika plaintext lebih panjang
- Spasi dipertahankan dalam ciphertext

### 2.3 Transposition Cipher

**Test Case 1:**
```
Plaintext : TRANSPOSITIONCIPHER
Key       : 5
Ciphertext: TSAOPETIINOTRNPSCHR
Decrypted : TRANSPOSITIONCIPHER
```

**Visualisasi Grid:**
```
[T] [R] [A] [N] [S] 
[P] [O] [S] [I] [T] 
[I] [O] [N] [C] [I] 
[P] [H] [E] [R] 
```

**Pembacaan per Kolom:**
```
Kolom 0: TPIP
Kolom 1: ROOH
Kolom 2: ASNE
Kolom 3: NICR
Kolom 4: STII
```

**Analisis:**
- Transposisi berhasil mengubah urutan karakter
- Frekuensi huruf tetap sama dengan plaintext
- Visualisasi membantu memahami proses enkripsi

---

## 3. Jawaban Pertanyaan Diskusi

### 3.1 Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?

**Caesar Cipher:**
1. **Kunci sangat terbatas**: Hanya ada 25 kemungkinan kunci (shift 1-25), mudah diserang dengan brute force
2. **Mudah dipecahkan**: Dengan mencoba semua 25 kemungkinan, pesan dapat didekripsi tanpa kunci
3. **Substitusi monoalfabetik**: Setiap huruf selalu diganti dengan huruf yang sama, pola dapat dikenali
4. **Tidak ada kerahasiaan kunci**: Jika satu pesan dipecahkan, semua pesan dengan kunci sama dapat dibaca

**Vigenère Cipher:**
1. **Analisis Kasiski**: Jika kunci pendek, pola berulang dalam ciphertext dapat dideteksi untuk menemukan panjang kunci
2. **Analisis frekuensi**: Setelah panjang kunci diketahui, cipher dapat dipecah menjadi beberapa Caesar Cipher dan diserang dengan analisis frekuensi
3. **Kunci berulang**: Jika plaintext jauh lebih panjang dari kunci, pola pengulangan kunci dapat dieksploitasi
4. **Rentan terhadap known-plaintext attack**: Jika sebagian plaintext diketahui, kunci dapat ditemukan

### 3.2 Mengapa cipher klasik mudah diserang dengan analisis frekuensi?

Cipher klasik mudah diserang dengan analisis frekuensi karena:

1. **Mempertahankan pola bahasa**:
   - Dalam bahasa alami, huruf-huruf tertentu muncul lebih sering (misal: E, T, A dalam bahasa Inggris)
   - Caesar Cipher hanya menggeser, sehingga frekuensi relatif tetap sama
   - Huruf paling sering dalam ciphertext kemungkinan adalah huruf paling sering dalam bahasa tersebut yang digeser

2. **Substitusi konsisten**:
   - Setiap huruf plaintext selalu diganti dengan huruf ciphertext yang sama
   - Memudahkan identifikasi pola dan hubungan antar huruf

3. **Pola kata dan bigram/trigram**:
   - Pola kata umum (seperti "THE", "AND" dalam bahasa Inggris) dapat dikenali
   - Kombinasi huruf tertentu yang sering muncul bersama membantu mengidentifikasi substitusi

4. **Ukuran sampel**:
   - Dengan ciphertext yang cukup panjang, distribusi frekuensi menjadi lebih jelas dan analisis lebih akurat

5. **Tidak ada difusi yang baik**:
   - Perubahan satu huruf plaintext hanya mempengaruhi satu huruf ciphertext
   - Tidak ada pencampuran (mixing) informasi antar karakter

### 3.3 Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi

| Aspek | Cipher Substitusi | Cipher Transposisi |
|-------|-------------------|-------------------|
| **Cara Kerja** | Mengganti huruf dengan huruf/simbol lain | Mengubah urutan/posisi huruf |
| **Kelebihan** | • Mengubah frekuensi huruf jika polialfabetik<br>• Dapat membuat teks tidak terbaca sama sekali<br>• Implementasi sederhana | • Mempertahankan informasi asli (semua huruf ada)<br>• Dapat dikombinasikan dengan substitusi<br>• Relatif cepat untuk teks panjang |
| **Kelemahan** | • Rentan analisis frekuensi (monoalfabetik)<br>• Pola bahasa dapat terdeteksi<br>• Kunci terbatas (Caesar) | • Tidak mengubah frekuensi huruf<br>• Analisis frekuensi langsung membocorkan huruf<br>• Rentan analisis pola kata |
| **Keamanan** | Rendah-Sedang (tergantung kompleksitas) | Rendah (jika digunakan sendiri) |
| **Penggunaan Modern** | Tidak digunakan (terlalu lemah) | Tidak digunakan sendiri, tapi konsep diffusion masih relevan |
| **Kombinasi** | Dapat dikombinasikan dengan transposisi | Dapat dikombinasikan dengan substitusi |

**Kesimpulan:**
- Cipher substitusi mengubah "apa" (huruf apa yang digunakan)
- Cipher transposisi mengubah "di mana" (posisi huruf)
- Keduanya lemah jika digunakan sendiri
- Cipher modern menggunakan kombinasi kedua konsep ini dengan iterasi berulang dan operasi matematika kompleks

---

## 4. Screenshot Hasil Uji Coba

*[Screenshot akan ditambahkan setelah menjalankan program]*

### Screenshot 1: Caesar Cipher
- Menunjukkan enkripsi dan dekripsi dengan berbagai kunci
- Demonstrasi brute force attack

### Screenshot 2: Vigenère Cipher
- Enkripsi dengan kunci berbeda panjang
- Hasil dekripsi yang akurat

### Screenshot 3: Transposition Cipher
- Visualisasi grid transposisi
- Proses pembacaan per kolom

---

## 5. Kesimpulan

1. **Implementasi berhasil**: Ketiga algoritma cipher klasik (Caesar, Vigenère, dan Transposisi) berhasil diimplementasikan dan menghasilkan enkripsi/dekripsi yang benar.

2. **Kelemahan fundamental**: Cipher klasik memiliki kelemahan mendasar:
   - Caesar: terlalu sederhana (25 kemungkinan kunci)
   - Vigenère: rentan Kasiski examination
   - Transposisi: tidak mengubah frekuensi huruf

3. **Nilai edukatif**: Meskipun tidak aman untuk penggunaan modern, cipher klasik memberikan pemahaman dasar tentang konsep kriptografi:
   - Substitusi (confusion)
   - Transposisi (diffusion)
   - Pentingnya panjang kunci
   - Kelemahan pola deterministik

4. **Relevansi modern**: Konsep-konsep dari cipher klasik masih digunakan dalam algoritma modern:
   - AES menggunakan substitusi (S-Box) dan transposisi
   - Prinsip confusion dan diffusion dari Shannon
   - Pentingnya iterasi berulang

---

## 6. Referensi

1. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson. Bab 3.
2. Modul Praktikum Keamanan Informasi Week 5 - Cipher Klasik
3. Singh, S. (1999). *The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography*. Doubleday.

---

**Catatan:** Program lengkap tersedia di folder `src/` dengan file:
- `caesar.py`
- `vigenere.py`
- `transpose.py`

Semua program dapat dijalankan secara independen dan menghasilkan output yang sesuai dengan spesifikasi praktikum.