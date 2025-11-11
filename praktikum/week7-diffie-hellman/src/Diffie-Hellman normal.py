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




def simulate_normal(p=23, g=5, verbose=True):
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
lines.append(f"Alice private a = {a}")
lines.append(f"Alice public A = {A}")
lines.append(f"Bob private b = {b}")
lines.append(f"Bob public B = {B}")
lines.append(f"Shared secret (Alice) = {SA}")
lines.append(f"Shared secret (Bob) = {SB}")
lines.append(f"Match: {SA == SB}")


out = "\n".join(lines)
if verbose:
print(out)
save_result('hasil_normal.txt', out)
return {'a':a,'b':b,'A':A,'B':B,'SA':SA,'SB':SB}



