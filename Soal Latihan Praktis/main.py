# Latihan Praktis:

# Buatlah program yang menanyakan nama dan umur pengguna, lalu tampilkan pesan seperti "Halo [nama], umur kamu [umur] tahun".
# Buat program yang menghitung rata-rata dari tiga angka yang dimasukkan oleh pengguna.
# Buat program yang menampilkan bilangan ganjil dari 1 hingga 10 menggunakan for loop.

# Jawaban
# 1. Program Menanyakan Nama dan Umur Pengguna:
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")

# Menampilkan pesan
print(f"Halo {nama}, umur kamu {umur} tahun.")

# 2. Program Menghitung Rata-rata dari Tiga Angka:
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Menghitung rata-rata
rata_rata = (angka1 + angka2 + angka3) / 3

# Menampilkan hasil rata-rata
print(f"Rata-rata dari ketiga angka tersebut adalah: {rata_rata}")

# 3. Program Menampilkan Bilangan Ganjil dari 1 hingga 10:
print("Bilangan ganjil dari 1 hingga 10 adalah:")
for angka in range(1, 11):
    if angka % 2 != 0:
        print(angka)


