#!/usr/bin/env python3
import random
import os
from datetime import datetime

# direktori output relatif terhadap lokasi file ini
try:
    BASE_DIR = os.path.dirname(__file__)
except NameError:
    BASE_DIR = os.getcwd()
OUT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'screenshots'))


def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def generate_private(p):
    """Buat private key acak dalam rentang [2, p-2].
    Validasi p agar randint tidak error.
    """
    if p <= 4:
        raise ValueError("p harus > 4 agar private key dapat dihasilkan (rentang 2..p-2).")
    return random.randint(2, p - 2)


def compute_public(g, private, p):
    return pow(g, private, p)


def compute_shared(public, private, p):
    return pow(public, private, p)


def save_result(filename, text):
    ensure_out_dir()
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Hasil disimpan: {path}")


def simulate_mitm(p=23, g=5, verbose=True):
    """Simulasi man-in-the-middle sederhana untuk Diffie-Hellman."""
    # Validasi parameter
    if p <= 4:
        raise ValueError("p harus lebih besar dari 4.")
    if not (2 <= g < p):
        raise ValueError("g harus dalam rentang 2 .. p-1 (dan < p).")

    # Alice dan Bob
    a = generate_private(p)
    b = generate_private(p)
    A = compute_public(g, a, p)
    B = compute_public(g, b, p)

    # Eve (attacker) membuat dua private key
    e1 = generate_private(p)
    e2 = generate_private(p)

    # Eve mengganti A dan B saat transit
    A_eve = compute_public(g, e1, p)   # dikirim ke Bob (mengaku A)
    B_eve = compute_public(g, e2, p)   # dikirim ke Alice (mengaku B)

    # Shared yang dihitung Alice dan Bob (dengan nilai yang telah dimodifikasi oleh Eve)
    SA = compute_shared(B_eve, a, p)   # Alice berpikir ini shared dengan Bob
    SB = compute_shared(A_eve, b, p)   # Bob berpikir ini shared dengan Alice

    # Shared yang dimiliki Eve dengan masing-masing pihak
    SE_with_alice = compute_shared(A, e1, p)  # Eve dengan Alice (Eve tahu A asli)
    SE_with_bob = compute_shared(B, e2, p)    # Eve dengan Bob (Eve tahu B asli)

    lines = []
    lines.append(f"Waktu: {datetime.now().isoformat()}")
    lines.append("-- SIMULASI MAN-IN-THE-MIDDLE (MITM) --")
    lines.append(f"p = {p}, g = {g}")
    lines.append("")
    lines.append("Alice:")
    lines.append(f"  private a = {a}")
    lines.append(f"  original public A = {A}")
    lines.append("")
    lines.append("Bob:")
    lines.append(f"  private b = {b}")
    lines.append(f"  original public B = {B}")
    lines.append("")
    lines.append("Eve (penyerang):")
    lines.append(f"  private e1 = {e1}")
    lines.append(f"  private e2 = {e2}")
    lines.append(f"  A_eve (yang dikirim ke Bob) = {A_eve}")
    lines.append(f"  B_eve (yang dikirim ke Alice) = {B_eve}")
    lines.append("")
    lines.append("Shared keys yang dihitung (hasil akhir di masing-masing pihak):")
    lines.append(f"  Alice menghitung shared (dengan B_eve) = {SA}")
    lines.append(f"  Bob menghitung shared (dengan A_eve)   = {SB}")
    lines.append("")
    lines.append("Shared keys yang dimiliki Eve:")
    lines.append(f"  Eve <-> Alice (menggunakan e1) = {SE_with_alice}")
    lines.append(f"  Eve <-> Bob   (menggunakan e2) = {SE_with_bob}")
    lines.append("")
    lines.append("Catatan: Jika SE_with_alice == SA atau SE_with_bob == SB, Eve berhasil memperoleh shared key.")
    output = "\n".join(lines)

    if verbose:
        print(output)

    # Simpan hasil ke file
    filename = f"mitm_sim_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    save_result(filename, output)
    return {
        "Alice": {"a": a, "A": A},
        "Bob": {"b": b, "B": B},
        "Eve": {"e1": e1, "e2": e2, "A_eve": A_eve, "B_eve": B_eve},
        "Shared": {"SA": SA, "SB": SB, "SE_with_alice": SE_with_alice, "SE_with_bob": SE_with_bob},
        "output_file": os.path.join(OUT_DIR, filename),
    }


if __name__ == "__main__":
    # Contoh pemanggilan
    result = simulate_mitm(p=23, g=5, verbose=True)
    # Jika ingin memeriksa hasil terstruktur:
    # import pprint; pprint.pprint(result)
