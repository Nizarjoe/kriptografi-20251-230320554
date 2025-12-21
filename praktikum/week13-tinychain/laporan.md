Laporan Praktikum Kriptografi

Minggu ke-: 13
Topik: TinyChain – Proof of Work (PoW)
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari praktikum ini adalah untuk memahami peran fungsi hash dalam teknologi blockchain, melakukan simulasi sederhana Proof of Work (PoW), serta menganalisis aspek keamanan dan kelemahan cryptocurrency yang berbasis kriptografi.

2. Dasar Teori

Blockchain merupakan struktur data terdistribusi yang terdiri dari rangkaian blok yang saling terhubung menggunakan fungsi hash kriptografis. Setiap blok menyimpan hash dari blok sebelumnya, sehingga perubahan pada satu blok akan memengaruhi seluruh rantai.

Fungsi hash kriptografis seperti SHA-256 memiliki sifat satu arah, deterministik, dan tahan terhadap collision. Dalam blockchain, hash digunakan untuk menjamin integritas data dan memastikan bahwa isi blok tidak dapat diubah tanpa terdeteksi.

Proof of Work (PoW) adalah mekanisme konsensus yang mengharuskan penambang (miner) menyelesaikan perhitungan komputasi tertentu sebelum sebuah blok dapat ditambahkan ke blockchain. Kesulitan perhitungan ini diatur oleh parameter difficulty, yang menentukan tingkat keamanan jaringan sekaligus memengaruhi konsumsi energi.

3. Alat dan Bahan

Python 3.11

Visual Studio Code

Git dan akun GitHub

Library Python bawaan:

hashlib

time

4. Langkah Percobaan

Membuat folder praktikum/week13-tinychain/ sesuai struktur yang ditentukan.

Membuat file tinychain.py di dalam folder src/.

Menuliskan kelas Block untuk merepresentasikan struktur blok blockchain.

Mengimplementasikan fungsi hash menggunakan SHA-256.

Menambahkan metode Proof of Work (mining) pada blok.

Membuat kelas Blockchain untuk mengelola rantai blok.

Menjalankan program dengan perintah:

python tinychain.py


Mengambil screenshot hasil proses mining blok.

Menyusun laporan praktikum pada file laporan.md.

Melakukan commit ke repository Git dengan pesan week13-tinychain.

5. Source Code

Berikut adalah source code utama yang digunakan dalam praktikum ini:

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


# Uji coba blockchain
my_chain = Blockchain()

print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

6. Hasil dan Pembahasan

Program berhasil dijalankan dan menampilkan proses mining untuk setiap blok. Setiap blok membutuhkan waktu tertentu untuk menemukan nilai nonce yang menghasilkan hash dengan awalan nol sesuai tingkat difficulty.

Semakin tinggi nilai difficulty, semakin banyak percobaan hash yang diperlukan, sehingga waktu mining menjadi lebih lama. Hal ini menunjukkan bagaimana Proof of Work berfungsi sebagai mekanisme keamanan untuk mencegah manipulasi data pada blockchain.

Screenshot hasil mining blok disimpan pada folder screenshots/.

7. Jawaban Pertanyaan

1. Mengapa fungsi hash sangat penting dalam blockchain?
Karena fungsi hash menjamin integritas data dan menghubungkan setiap blok secara kriptografis, sehingga perubahan data dapat langsung terdeteksi.

2. Bagaimana Proof of Work mencegah double spending?
PoW membuat perubahan data membutuhkan usaha komputasi besar dan harus disetujui jaringan, sehingga transaksi ganda sulit dilakukan tanpa menguasai mayoritas kekuatan komputasi.

3. Apa kelemahan dari PoW dalam hal efisiensi energi?
PoW membutuhkan daya komputasi tinggi yang menyebabkan konsumsi energi besar, sehingga kurang ramah lingkungan dan tidak efisien untuk skala besar.

8. Kesimpulan

Praktikum ini menunjukkan bahwa fungsi hash dan Proof of Work merupakan komponen utama dalam keamanan blockchain. Meskipun PoW efektif menjaga integritas data, mekanisme ini memiliki kelemahan dari sisi efisiensi energi yang perlu dipertimbangkan dalam pengembangan sistem blockchain modern.

9. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security. Pearson Education.

Stinson, D. R. (2019). Cryptography: Theory and Practice. CRC Press.

10. Commit Log
commit abcdef131313
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-01-03

    week13-tinychain