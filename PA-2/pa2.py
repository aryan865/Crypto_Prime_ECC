from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from tinyec import registry

def load_certificate(cert_path):
    with open(cert_path, "rb") as file:
        cert_data = file.read()

    try:
        # Try loading as PEM
        return x509.load_pem_x509_certificate(cert_data, default_backend())
    except ValueError:
        # If PEM fails, try DER
        return x509.load_der_x509_certificate(cert_data, default_backend())


def get_curve_info(cert_path):
    cert = load_certificate(cert_path)
    public_key = cert.public_key()

    if not isinstance(public_key, ec.EllipticCurvePublicKey):
        print("This certificate does NOT use Elliptic Curve cryptography.")
        return

    curve = public_key.curve
    print("\n=== ECC Certificate Details ===")
    print("Elliptic Curve Used:", curve.name)

    # Try reading a and b if exposed
    try:
        curve = registry.get_curve(curve.name)
        p = curve.field.p
        a = curve.a
        b = curve.b

        # print("\nElliptic Curve Equation:")
        # print(f"y^2 = x^3 + {a}x + {b} (mod {p})")

        print(f"a = {a}")
        print(f"b = {b}")
        print(f"p = {p}")
    except Exception as e:
        print("Curve not found in tinyec registry:", e)


if __name__ == "__main__":
    path = input("Enter the .crt file path: ")
    get_curve_info(path)
