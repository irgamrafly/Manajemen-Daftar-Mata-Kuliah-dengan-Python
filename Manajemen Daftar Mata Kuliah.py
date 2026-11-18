# Daftar mata kuliah awal
mata_kuliah = ["Algoritma", "Basis Data", "Jaringan"]

# Menampilkan daftar mata kuliah awal
print("Daftar Mata Kuliah:")
i = 0
while i < len(mata_kuliah):
    print(i + 1, ".", mata_kuliah[i])
    i += 1

print("Jumlah mata kuliah:", len(mata_kuliah))

# Menambahkan mata kuliah melalui input
matkul_tambah = input("Masukkan mata kuliah yang ingin ditambahkan: ").strip()

if matkul_tambah != "":
    mata_kuliah.append(matkul_tambah)
    print("Mata kuliah ditambah:", matkul_tambah)
else:
    print("Nama mata kuliah tidak boleh kosong.")

# Menampilkan daftar terbaru
print("Daftar terbaru:")
i = 0
while i < len(mata_kuliah):
    print(i + 1, ".", mata_kuliah[i])
    i += 1

# Menghapus mata kuliah melalui input
matkul_hapus = input("Masukkan mata kuliah yang ingin dihapus: ").strip()

if matkul_hapus in mata_kuliah:
    mata_kuliah.remove(matkul_hapus)
    print("Mata kuliah dihapus:", matkul_hapus)
else:
    print("Mata kuliah tidak ditemukan:", matkul_hapus)

# Menampilkan daftar akhir
print("Daftar akhir:")
i = 0
while i < len(mata_kuliah):
    print(i + 1, ".", mata_kuliah[i])
    i += 1

print("Jumlah mata kuliah akhir:", len(mata_kuliah))
