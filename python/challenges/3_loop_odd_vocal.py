
# Program List Angka Ganjil dan Hitung Vokal

#  List semua angka ganjil 1-15 dalam satu baris kode
angka_ganjil = [i for i in range(1, 16) if i % 2 != 0]
print(angka_ganjil)


kata = input("Masukkan kata: ")

# TODO: Program menghitung jumlah huruf vokal
vokal = "aiueoAIUEO"
jumlah_vokal = sum(1 for huruf in kata if huruf in vokal)

print(f"Jumlah huruf vokal: {jumlah_vokal}")