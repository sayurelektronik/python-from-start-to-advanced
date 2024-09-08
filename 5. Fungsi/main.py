# Fungsi adalah blok kode yang bisa digunakan kembali dan dapat menerima input serta mengembalikan output.

# Contoh membuat fungsi:

# Fungsi sederhana tanpa parameter
def sapa():
    print("Halo, selamat datang!")

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}, selamat datang!")

# Fungsi dengan return
def tambah(a, b):
    return a + b

# Memanggil fungsi
sapa()  # Output: Halo, selamat datang!
sapa_nama("Andi")  # Output: Halo, Andi, selamat datang!
hasil = tambah(5, 3)
print(hasil)  # Output: 8
