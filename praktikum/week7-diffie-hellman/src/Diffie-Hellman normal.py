#!/usr/bin/env python3
import random
import os
from datetime import datetime

# Tentukan OUT_DIR relatif terhadap file ini; jika __file__ tidak ada, gunakan cwd
try:
    BASE_DIR = os.path.dirname(__file__)
except NameError:
    BASE_DIR = os.getcwd()
OUT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'screenshots'))


def ensure_out_dir():
    """Buat folder output jika belum ada."""
    os.makedirs(OUT_DIR, exist_ok=True)


def generate_private(p):
    """Generate private key dalam rentang [2, p-2]. Validasi p."""
    if p <= 4:
        raise ValueError("p harus > 4 agar private key dapat dihasilkan (rentang 2..p-2).")
    return random.randint(2, p - 2)


def compute_public(g, private, p):
    return pow(g, private, p)


def compute_shared(public, private, p):
    return pow(public, private, p)


def save_result(filename, text):
    """Simpan teks ke file di OUT_DIR (UTF-8)."""
    ensure_out_dir()
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Hasil disimpan: {path}")


def simulate_normal(p=23, g=5, verbose=True):
    """
    Simulasi Diffie-Hellman normal (tanpa attacker).
    Mengembalikan dict berisi nilai-nilai yang dihasilkan dan menyimpan hasil ke file.
    """
    # Validasi parameter sederhana
    if p <= 4:
        raise ValueError("p harus lebih besar dari 4.")
    if not (2 <= g < p):
        raise ValueError("g harus dalam rentang 2 .. p-1 (dan < p).")

    a = generate_private(p)
    b = generate_private(p)
    A = compute_public(g, a, p)
    B = compute_public(g, b, p)
    SA = compute_shared(B, a, p)
    SB = compute_shared(A, b, p)

    lines = []
    lines.append(f"Waktu: {datetime.now().isoformat()}")
    lines.append("-- SIMULASI DIFFIE-HELLMAN (NORMAL) --")
    lines.append(f"p = {p}, g = {g}")
    lines.append("")
    lines.append("Alice:")
    lines.append(f"  private a = {a}")
    lines.append(f"  public  A = {A}")
    lines.append("")
    lines.append("Bob:")
    lines.append(f"  private b = {b}")
    lines.append(f"  public  B = {B}")
    lines.append("")
    lines.append("Shared secrets:")
    lines.append(f"  Alice menghitung shared = {SA}")
    lines.append(f"  Bob   menghitung shared = {SB}")
    lines.append(f"  Match = {SA == SB}")

    out = "\n".join(lines)
    if verbose:
        print(out)

    # Simpan hasil
    filename = f"diffie_normal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    save_result(filename, out)

    return {"a": a, "b": b, "A": A, "B": B, "SA": SA, "SB": SB, "output_file": os.path.join(OUT_DIR, filename)}


if __name__ == "__main__":
    # Contoh pemanggilan
    result = simulate_normal(p=23, g=5, verbose=True)
    # Jika ingin melihat hasil terstruktur: import pprint; pprint.pprint(result)
