# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
usia = int(input("Masukkan usia: "))


# 2. TODO Tentukan kategori berdasarkan usia

if usia < 12:
    kategori = "Anak-anak"
elif usia >= 12 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
else:  # usia >= 60
    kategori = "Lansia"


# Menampilkan hasil
print(f"Kategori: {kategori}")