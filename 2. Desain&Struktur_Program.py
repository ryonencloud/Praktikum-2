# ==========================================
# 1. DESAIN PROGRAM: FUNGSI MODULAR
# ==========================================

def ganjil_genap(n):
    return "Genap" if n % 2 == 0 else "Ganjil"

def prima(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        # Diperbaiki: Menambahkan indentasi di dalam blok while
        if n % i == 0:
            return False
        i += 1
    return True

def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kpk(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // fpb(a, b)

def desimal_ke_hex(n):
    digit = "0123456789ABCDEF"
    hasil = ""
    while n > 0:
        # Diperbaiki: Menambahkan indentasi di dalam blok while
        hasil = digit[n % 16] + hasil
        n //= 16
    return hasil or "0"


# ==========================================
# 2. STRUKTUR PROGRAM UTAMA
# ==========================================

data = [260306024, 11, 10, 2026, 25, 5, 2007]

print("=" * 50)
print("ANALISIS BILANGAN")
print("=" * 50)

for n in data:
    print(f"\nBilangan : {n}")
    print(f"Status   : {ganjil_genap(n)}")
    print(f"Prima    : {'Ya' if prima(n) else 'Tidak'}")
    print(f"Hex      : {desimal_ke_hex(n)}")

# FPB dan KPK keseluruhan
hasil_fpb = data[0]
hasil_kpk = data[0]

for x in data[1:]:
    hasil_fpb = fpb(hasil_fpb, x)
    hasil_kpk = kpk(hasil_kpk, x)

print(f"\nFPB semua bilangan : {hasil_fpb}")
print(f"KPK semua bilangan : {hasil_kpk}")