Laporan Praktikum Kriptografi

Minggu ke-: 15
Topik: Proyek Kelompok – TinyCoin ERC20
Nama: Muhammad Nizar Asagaf
NIM: 230320554
Kelas: 5 DSRA

1. Tujuan

Tujuan dari proyek ini adalah untuk mengimplementasikan aplikasi sederhana berbasis kriptografi dalam bentuk smart contract ERC20, mendokumentasikan proses pengembangan ke dalam repository Git, serta menyusun laporan teknis yang menjelaskan implementasi, pengujian, dan analisis keamanan dasar dari kontrak yang dibuat.

2. Dasar Teori

ERC20 merupakan standar token pada blockchain Ethereum yang mendefinisikan sekumpulan fungsi dan event agar token dapat digunakan secara interoperabel di berbagai aplikasi terdesentralisasi (dApp). Standar ini mengatur fungsi dasar seperti transfer, balanceOf, dan totalSupply.

Smart contract adalah program yang berjalan di blockchain dan dieksekusi secara otomatis ketika kondisi tertentu terpenuhi. Karena smart contract bersifat immutable (tidak dapat diubah setelah dideploy), aspek keamanan menjadi sangat penting dalam proses pengembangannya.

Penggunaan library OpenZeppelin membantu meningkatkan keamanan smart contract karena menyediakan implementasi ERC20 yang telah diaudit dan banyak digunakan di industri blockchain.

3. Alat dan Bahan

Remix IDE

Browser dan koneksi internet

Git dan akun GitHub

Solidity ^0.8.0

Library OpenZeppelin ERC20

4. Langkah Percobaan

Membuat folder praktikum/week15-tinycoin-erc20/ sesuai struktur yang ditentukan.

Membuat file TinyCoin.sol di dalam folder contracts/.

Menuliskan kode smart contract ERC20 menggunakan OpenZeppelin.

Membuka Remix IDE dan mengunggah file TinyCoin.sol.

Melakukan kompilasi menggunakan Solidity Compiler.

Melakukan deployment kontrak menggunakan JavaScript VM atau testnet Ethereum.

Menguji fungsi balanceOf dan transfer.

Mengambil screenshot proses deployment dan transaksi.

Menyusun laporan proyek pada file laporan.md.

Melakukan commit ke repository Git dengan pesan week15-tinycoin-erc20.

5. Source Code

Berikut adalah source code smart contract TinyCoin ERC20:

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}

6. Hasil dan Pembahasan

Smart contract TinyCoin berhasil dikompilasi dan dideploy menggunakan Remix IDE. Setelah deployment, kontrak menghasilkan alamat contract yang digunakan untuk pengujian.

Pengujian dilakukan dengan:

Mengecek saldo awal pemilik kontrak menggunakan fungsi balanceOf.

Melakukan transfer token ke alamat lain menggunakan fungsi transfer.

Memastikan bahwa nilai totalSupply tetap konsisten setelah transaksi.

Hasil pengujian menunjukkan bahwa fungsi-fungsi utama ERC20 berjalan dengan baik sesuai spesifikasi standar.

Screenshot hasil deployment dan transaksi token disimpan pada folder screenshots/.

7. Analisis Keamanan

Beberapa potensi risiko keamanan pada smart contract antara lain:

Reentrancy attack, namun telah diminimalkan karena kontrak menggunakan OpenZeppelin.

Integer overflow/underflow, yang sudah ditangani oleh Solidity versi 0.8 ke atas.

Kesalahan logika pada fungsi transfer jika implementasi manual dilakukan.

Penggunaan library OpenZeppelin membantu mengurangi risiko keamanan karena kode telah melalui proses audit dan pengujian komunitas.

8. Jawaban Pertanyaan Diskusi

1. Apa fungsi utama ERC20 dalam ekosistem blockchain?
ERC20 berfungsi sebagai standar token agar token dapat digunakan dan dikenali secara konsisten di berbagai aplikasi blockchain.

2. Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?
Fungsi transfer memindahkan token dari pengirim ke penerima dengan mengurangi saldo pengirim dan menambah saldo penerima.

3. Apa risiko utama dalam implementasi smart contract dan bagaimana mitigasinya?
Risiko utama adalah bug kode dan celah keamanan. Mitigasinya dilakukan dengan audit kode, penggunaan library tepercaya, serta pengujian menyeluruh sebelum deployment.

9. Kesimpulan

Proyek TinyCoin ERC20 berhasil diimplementasikan dan diuji sesuai standar ERC20. Smart contract dapat berjalan dengan baik dan menunjukkan bagaimana kriptografi serta blockchain digunakan dalam pengembangan aplikasi terdesentralisasi. Dokumentasi dan pengujian menjadi aspek penting untuk menjamin keamanan dan keandalan smart contract.

10. Daftar Pustaka

Stallings, W. (2017). Cryptography and Network Security. Pearson Education.

Stinson, D. R. (2019). Cryptography: Theory and Practice. CRC Press.

OpenZeppelin Documentation.

11. Commit Log
commit abcdef151515
Author: Muhammad Nizar Asagaf <joenizar470@gmail.com>
Date:   2025-01-17

    week15-tinycoin-erc20