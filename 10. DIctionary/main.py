# Dictionary menyimpan data dalam pasangan key-value.

# Digunakan ketika:
# 1. Membutuhkan asosiasi kunci dengan nilai (key-value pairs) untuk mengakses elemen.
# 2. Data bersifat tidak terurut dan kamu memerlukan akses cepat berdasarkan kunci.
# 3. Setiap elemen memiliki identitas unik berupa kunci, dan kamu ingin mengakses elemen menggunakan kunci tersebut, bukan indeks.

# Karakteristik:
# 1. Mutable: bisa diubah setelah dideklarasikan (menambah/menghapus/mengedit elemen).
# 2. Setiap elemen diakses melalui kunci (key), bukan indeks.
# 3. Kunci harus unik, tapi nilai boleh duplikat.

# Kapan digunakan:
# 1. Ketika kamu memerlukan akses cepat berdasarkan kunci unik.
# 2. Saat data berhubungan dengan konsep entitas dengan atribut yang jelas.
# 3. Misalnya: data mahasiswa dengan atribut (nama, umur, alamat), kamus kosakata (kata dan definisi).

# Contoh:

# Membuat dictionary
data_mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Informatika"
}

# Akses nilai menggunakan key
print(data_mahasiswa["nama"])  # Output: Andi

# Menambahkan pasangan key-value baru
data_mahasiswa["semester"] = 5

print(data_mahasiswa)
# Output: {'nama': 'Andi', 'umur': 21, 'jurusan': 'Informatika', 'semester': 5}
