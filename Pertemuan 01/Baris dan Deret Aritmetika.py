def barisan_aritmetika(a: float, b: float, n: int):
    Un = a + (n - 1) * b
    Sn = (n / 2) * (2*a + (n - 1) * b)
    return Un, Sn

if __name__ == "__main__":
    a = float(input("Masukkan suku pertama (a): "))
    b = float(input("Masukkan beda (b): "))
    n = int(input("Masukkan n (banyak suku / urutan suku): "))

    Un, Sn = barisan_aritmetika(a, b, n)

    print(f"Suku ke-{n} = {Un}")
    print(f"Jumlah {n} suku pertama = {Sn}")