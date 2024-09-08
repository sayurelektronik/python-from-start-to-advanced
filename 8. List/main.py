# List adalah kumpulan elemen yang bisa diubah (mutable) dan bisa berisi berbagai tipe data.

# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen list
print(buah[0])  # Output: apel
print(buah)  # Output: ['apel', 'jeruk', 'mangga']

# Menambah elemen baru ke list
buah.append("pisang")
print(buah) # Output: ['apel', 'jeruk', 'mangga', 'pisang']

# Menambah elemen baru di indeks ke-2
buah.insert(1, "Nanash")
print(buah) # Output: ['apel', 'Nanash', 'jeruk', 'mangga', 'pisang']

# Mengubah elemen list
buah[1] = "anggur"

print(buah)  # Output: ['apel', 'anggur', 'jeruk', 'mangga', 'pisang']
