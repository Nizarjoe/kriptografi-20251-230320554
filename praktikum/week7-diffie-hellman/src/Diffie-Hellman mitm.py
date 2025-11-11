import random
import os
from datetime import datetime


OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
OUT_DIR = os.path.abspath(OUT_DIR)




def ensure_out_dir():
os.makedirs(OUT_DIR, exist_ok=True)




def generate_private(p):
return random.randint(2, p-2)




def compute_public(g, private, p):
return pow(g, private, p)




def compute_shared(public, private, p):
return pow(public, private, p)




def save_result(filename, text):
ensure_out_dir()
path = os.path.join(OUT_DIR, filename)
with open(path, 'w') as f:
f.write(text)
print(f"Hasil disimpan: {path}")




def simulate_mitm(p=23, g=5, verbose=True):
# Alice dan Bob
a = generate_private(p)
b = generate_private(p)
A = compute_public(g, a, p)
B = compute_public(g, b, p)


# Eve (attacker) membuat dua private key
e1 = generate_private(p)
e2 = generate_private(p)


# Eve mengganti A dan B saat transit
A_eve = compute_public(g, e1, p)
B_eve = compute_public(g, e2, p)


# Shared yang dihitung Alice dan Bob (dengan nilai yang telah dimodifikasi oleh Eve)
SA = compute_shared(B_eve, a, p)
SB = compute_shared(A_eve, b, p)


# Shared yang dimiliki Eve dengan masing-masing pihak
SE_with_alice = compute_shared(A, e1, p)
SE_with_bob = compute_shared(B, e2, p)


lines = []
lines.append(f"Waktu: {datetime.now().isoformat()}")
lines.append("-- SIMULASI MAN-IN-THE-MIDDLE (MITM) --")
lines.append(f"p = {p}, g = {g}")
lines.append(f"Alice private a = {a}")
lines.append(f"Alice original public A = {A}")
lines.append(f"Bob private b = {b}")
lines.append(f"Bob original public B = {B}")
lines.append("Eve intercept dan mengganti public key:")
lines.append(f" A_eve (dikirim ke Bob) = {A_eve} [dihasilkan dari e1={e1}]")
lines.append(f" B_eve (dikirim ke Alice) = {B_eve} [dihasilkan dari e2={e2}]")
lines.append(f"Shared yang dihitung Alice (dengan B_eve) = {SA}")