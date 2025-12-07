# Crypto_Prime_ECC

Below is an improved **README.md**, rewritten to align directly with the description, goals, motivation, and evaluation criteria given in **your assignment PDF** .

---

# 📌 Programming Assignment – **Cryptography**

## **PA-1 – Willans’ Formula & Prime Computation**

## **PA-2 – Elliptic Curve Cryptography Certificate Analysis**

---

## 🔷 **Course Context**

In the cryptography course, a major focus was understanding the RSA cryptosystem and how its security depends fundamentally on the difficulty of **prime factorization**. This naturally leads to the study of **primality testing**, **prime detectors**, and ultimately the mathematical curiosity — **can a prime detector be transformed into a prime computer?**

During the 1960s, researchers explored formulae capable of generating the **nth prime number**. One of these artificially designed approaches, **Willans' Formula**, applies **Wilson’s Theorem** for prime detection and embeds it inside a computational expression to obtain primes sequentially. Although these formulas are not practical for large-scale use, they introduce an important conceptual question:

> **Can we systematically turn a primality-testing mechanism into a prime-computing mechanism?**
> (i.e., Input: `n`, Output: nth prime)

This repository attempts exactly that.

---

## 🔹 PA-1 — **Nth Prime Number Using a Formula (Python)**

### **Objective**

✔ Construct a formula that transforms a prime detector into a prime computer
✔ Implement and test the formula
✔ Analyze and compare time complexity with Willans’ formula

### **Approach**

* **Wilson’s Theorem** is used to detect primality:
  [(p - 1)! ≡ -1 (mod\ p)] if and only if `p` is prime
* A recursively memoized prime-counting function π(x) keeps the solution efficient
* Rosser–Schoenfeld upper bound ensures the algorithm stops at or before the nth prime
* The formula computes:
  [
  \text{nth prime} = 2 + \sum_{i=2}^{U}
  \bigg\lfloor \left(\frac{n}{\pi(i)+1}\right)^{1/n} \bigg\rfloor
  ]

### **Time Complexity Discussion**

| Formula             | Complexity                                                                           | Remarks                                                     |
| ------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Willans’ Formula    | **Exponential / factorial growth**                                                   | Impractical                                                 |
| This implementation | **Significantly lower; dominated by Wilson modular factorial check + repeated π(i)** | Still mathematically interesting, not optimized for large n |

While this method is still slower than modern sieves, it **successfully demonstrates transformation from detector → computer**, which is the key learning goal of PA-1.

### **Execution**

```bash
python pa1_prime_formula.py
```

Provide an input `n`:

```
Enter n to find nth prime: 20
20th prime = 71
```

---

## 🔹 PA-2 — **Extract ECC Curve Equation & Field Characteristic (Python)**

### **Objective**

✔ Export and analyze a live website’s SSL certificate
✔ Extract the **elliptic curve equation parameters**
✔ Extract the **characteristic of the finite field**

This relates to **EC-DSA digital signatures**, widely deployed in modern authentication (HTTPS certificates, identity verification, etc.) — as referenced in the assignment description .

### **How the Program Works**

* Loads `.crt` in **PEM or DER** format
* Identifies the ECC curve used (e.g., `secp256r1`)
* Retrieves:

  * **a** (curve parameter)
  * **b** (curve parameter)
  * **p** (prime modulus, i.e., characteristic of GF(p))
* Outputs elliptic curve equation:

[
y^2 \equiv x^3 + ax + b \mod p
]

### **Execution**

Install dependencies:

```bash
pip install cryptography tinyec
```

Run the script:

```bash
python pa2_extract_ecc.py
```

Example output:

```
=== ECC Certificate Details ===
Elliptic Curve Used: secp256r1
a = -3
b = 410583637251521...
p = 115792089210356248762697446949407573530...
```

---

## 📁 Repository Structure

```
├── PA-1
│   └── pa1_prime_formula.py
├── PA-2
│   └── pa2_extract_ecc.py
└── README.md
```

---

## 📌 Evaluation Criteria (As per assignment PDF)

| Assignment         | Submission Weight                                        |
| ------------------ | -------------------------------------------------------- |
| PA-1 & PA-2        | 50% for submission                                       |
| Viva / Code Review | 50% based on explanation and modularity                  |
| **Bonus**          | If PA-1 formula outperforms Willans’ → PA-2 not required |

---

## 🧠 Final Notes for Viva / Demonstration

You should be prepared to explain:

| Topic                   | Why it matters                     |
| ----------------------- | ---------------------------------- |
| Wilson’s Theorem        | Basis of prime detection           |
| Rosser–Schoenfeld Bound | Ensures termination                |
| π(x) Prime counting     | Converts checking → computing      |
| ECC                     | Used in modern authentication      |
| GF(p)                   | Finite field arithmetic efficiency |

---

If you'd like, I can **add a small theory appendix** inside README explaining **RSA ↔ prime generation ↔ ECC security** — useful for viva answers. Just tell me 👍
