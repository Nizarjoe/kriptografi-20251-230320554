import random

# Bilangan prima besar (field modulo)
PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481


def mod_inverse(a, p):
    """Mencari invers modulo"""
    return pow(a, -1, p)


def generate_polynomial(secret, k):
    """Membuat polinomial derajat k-1 dengan konstanta = secret"""
    coeffs = [secret]
    for _ in range(k - 1):
        coeffs.append(random.randrange(0, PRIME))
    return coeffs


def evaluate_polynomial(coeffs, x):
    """Evaluasi polinomial pada titik x"""
    y = 0
    for i, coef in enumerate(coeffs):
        y = (y + coef * pow(x, i, PRIME)) % PRIME
    return y


def split_secret(secret, k, n):
    """Membagi secret menjadi n share dengan threshold k"""
    coeffs = generate_polynomial(secret, k)
    shares = []

    for i in range(1, n + 1):
        x = i
        y = evaluate_polynomial(coeffs, x)
        shares.append((x, y))

    return shares


def recover_secret(shares):
    """Rekonstruksi secret menggunakan interpolasi Lagrange"""
    secret = 0

    for i, (xi, yi) in enumerate(shares):
        li = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                li = li * (-xj) * mod_inverse(xi - xj, PRIME)
                li %= PRIME
        secret = (secret + yi * li) % PRIME

    return secret


def main():
    # Rahasia (diubah ke integer)
    secret_text = "KriptografiUPB2025"
    secret_int = int.from_bytes(secret_text.encode(), "big")

    k = 3  # threshold
    n = 5  # total share

    print("Secret Asli:", secret_text)

    shares = split_secret(secret_int, k, n)

    print("\nShares yang dihasilkan:")
    for share in shares:
        print(share)

    # Ambil k share untuk rekonstruksi
    selected_shares = shares[:k]
    recovered_int = recover_secret(selected_shares)

    recovered_text = recovered_int.to_bytes(
        (recovered_int.bit_length() + 7) // 8, "big"
    ).decode()

    print("\nRecovered Secret:", recovered_text)


if __name__ == "__main__":
    main()
