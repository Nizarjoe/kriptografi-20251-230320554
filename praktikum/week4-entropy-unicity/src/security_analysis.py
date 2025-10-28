import math
import time

# =====================================================
# Analisis Entropy, Unicity Distance, dan Brute Force
# =====================================================

def key_entropy(symbols, length):
    """Hitung entropi kunci (bit)"""
    return math.log2(symbols ** length)

def unicity_distance(entropy_bits, redundancy):
    """Hitung unicity distance"""
    return entropy_bits / redundancy

def brute_force_time(key_bits, guesses_per_second=1e9):
    """Estimasi waktu brute force rata-rata (detik)"""
    total_keys = 2 ** key_bits
    avg_attempts = total_keys / 2
    seconds = avg_attempts / guesses_per_second
    return seconds

# ---- Contoh Kasus ----
if __name__ == "__main__":
    symbols = 62  # huruf besar + kecil + angka
    length = 10   # panjang kunci
    redundancy = 1.5  # redundansi per karakter (bit)
    guesses_per_second = 1e9  # 1 miliar tebakan per detik

    print("=== Analisis Kekuatan Kunci ===")
    entropy_bits = key_entropy(symbols, length)
    print(f"Entropi kunci: {entropy_bits:.2f} bit")

    U = unicity_distance(entropy_bits, redundancy)
    print(f"Unicity distance: {U:.2f} karakter ciphertext")

    t = brute_force_time(entropy_bits, guesses_per_second)
    print(f"Estimasi waktu brute force: {t:.2e} detik (~{t/3600/24/365:.2e} tahun)")
