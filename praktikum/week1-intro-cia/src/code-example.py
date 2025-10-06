# cia_demo.py
# Praktikum Kriptografi - Prinsip CIA (Confidentiality, Integrity, Availability)
# Nama : Muhammad Nizar Asagaf
# NIM  : 230320554
# Week : 1

# Import library yang dibutuhkan
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import shutil
import os

print("=== PRAKTIKUM KRIPTOGRAFI ===")
print("DEMONSTRASI PRINSIP CIA (Confidentiality, Integrity, Availability)")
print("---------------------------------------------------------------\n")

# ---------------------------------------------------------------
# 1. CONFIDENTIALITY (Kerahasiaan)
# ---------------------------------------------------------------
print("1. CONFIDENTIALITY (Kerahasiaan)")
print("Tujuan: menjaga agar pesan hanya bisa dibaca oleh pihak yang berhak.\n")

key = get_random_bytes(16)  # Membuat kunci acak 16 byte
data = b"Pesan Rahasia CIA"

# Enkripsi menggunakan algoritma AES (mode EAX)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print("Teks Asli       :", data)
print("Teks Terenkripsi:", ciphertext)
print("Kunci (hex)     :", key.hex())
print("Keterangan      : Pesan berhasil dienkripsi agar tidak bisa dibaca orang lain.\n")

# ---------------------------------------------------------------
# 2. INTEGRITY (Integritas)
# ---------------------------------------------------------------
print("2. INTEGRITY (Integritas)")
print("Tujuan: memastikan data tidak diubah tanpa izin.\n")

data_asli = "Pesan Rahasia CIA"
hash_asli = hashlib.sha256(data_asli.encode()).hexdigest()
print("Hash Data Asli :", hash_asli)

# Simulasi data diubah
data_diubah = "Pesan Rahasia CI4"
hash_diubah = hashlib.sha256(data_diubah.encode()).hexdigest()
print("Hash Data Diubah:", hash_diubah)

if hash_asli == hash_diubah:
    print("Integritas Terjaga ✅ (Data belum berubah)\n")
else:
    print("Integritas Rusak ❌ (Data telah dimodifikasi)\n")

# ---------------------------------------------------------------
# 3. AVAILABILITY (Ketersediaan)
# ---------------------------------------------------------------
print("3. AVAILABILITY (Ketersediaan)")
print("Tujuan: menjaga agar data tetap bisa diakses saat dibutuhkan.\n")

file_asli = "laporan.md"
backup_dir = "backup/"
backup_file = os.path.join(backup_dir, "laporan_backup.md")

os.makedirs(backup_dir, exist_ok=True)

try:
    shutil.copy(file_asli, backup_file)
    print(f"Backup Berhasil ✅ : {file_asli} disalin ke {backup_file}")
except FileNotFoundError:
    print(f"⚠️ File {file_asli} belum ada, buat dulu sebelum menjalankan backup.\n")

print("\n=== SELESAI ===")
print("Ketiga prinsip CIA sudah didemonstrasikan dengan sederhana.")
