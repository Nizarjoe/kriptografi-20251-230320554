import ssl
import socket
from datetime import datetime


def check_tls_certificate(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            tls_version = ssock.version()

    issuer = dict(x[0] for x in cert['issuer'])
    subject = dict(x[0] for x in cert['subject'])

    valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
    valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

    print("=" * 50)
    print(f"Website            : {hostname}")
    print(f"Protokol           : HTTPS (TLS)")
    print(f"TLS Version        : {tls_version}")
    print(f"Cipher Suite       : {cipher[0]}")
    print(f"Algoritma Enkripsi : {cipher[1]}")
    print(f"Key Length         : {cipher[2]} bit")
    print("\nInformasi Sertifikat:")
    print(f"Issuer CA          : {issuer.get('organizationName', 'Unknown')}")
    print(f"Subject            : {subject.get('commonName', 'Unknown')}")
    print(f"Masa Berlaku Dari  : {valid_from}")
    print(f"Masa Berlaku Hingga: {valid_to}")
    print("=" * 50)
    print()


def main():
    websites = [
        "www.tokopedia.com",
        "www.shopee.co.id"
    ]

    print("ANALISIS TLS WEBSITE E-COMMERCE\n")

    for site in websites:
        check_tls_certificate(site)


if __name__ == "__main__":
    main()
