# Tuple mirip dengan list, tetapi elemen-elemen di dalam tuple tidak bisa diubah (immutable).

# Digunakan ketika:
# 1. Data bersifat berurutan, tapi tidak boleh diubah (immutable) setelah dideklarasikan.
# 2. Membutuhkan performa yang lebih baik dibanding list dalam operasi akses karena tuple lebih ringan dan lebih cepat.
# 3. Data digunakan sebagai konstanta atau kumpulan elemen yang tidak akan berubah.

# Karakteristik:
# 1. Immutable: tidak bisa diubah setelah dideklarasikan (tidak bisa menambah, menghapus, atau mengubah elemen).
# 2. Diakses melalui indeks seperti list.
# 3. Lebih cepat dari list dalam operasi tertentu.
# 4. Bisa menyimpan elemen duplikat.

# Kapan digunakan:
# 1. Ketika data harus konstan dan tidak boleh berubah.
# 2. Saat urutan data penting, tapi tidak akan ada operasi perubahan pada data.
# Misalnya: koordinat geografis, pengelompokan beberapa nilai tetap (misalnya RGB pada gambar).

# Gunakan ketika data berurutan tapi tidak boleh diubah. Cocok untuk menyimpan nilai tetap yang tidak akan berubah.

# Contoh:
# Membuat tuple
angka = (1, 2, 3, 4)

# Akses elemen tuple
print(angka[1])  # Output: 2