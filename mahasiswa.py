# Project Python: Demonstrasi Konsep Referensi Objek, Fungsi dengan Default Parameter, 
# Perhitungan Rata-Rata, Penggabungan List Tanpa Duplikasi, dan Cetak Daftar Siswa

# 1. Fungsi ubah_nilai: Mengubah elemen pertama list menjadi 100 (demonstrasi referensi objek)
def ubah_nilai(my_list):
    """
    Fungsi untuk mengubah elemen pertama dari list menjadi 100.
    Karena list adalah mutable, perubahan ini akan memengaruhi list asli.
    """
    if len(my_list) > 0:  # Pastikan list tidak kosong
        my_list[0] = 100
        print("Elemen pertama berhasil diubah menjadi 100 di dalam fungsi.")
    else:
        print("List kosong, tidak ada elemen untuk diubah.")

# 2. Fungsi perkenalan: Menerima nama dan usia (default 0), cetak perkenalan
def perkenalan(nama, usia=0):
    """
    Fungsi untuk mencetak perkenalan diri dengan nama dan usia.
    Usia memiliki nilai default 0.
    """
    print(f"Halo, nama saya {nama}. Usia saya {usia} tahun.")

# 3. Fungsi hitung_rata_rata: Hitung rata-rata nilai dari list, handle list kosong
def hitung_rata_rata(nilai_siswa):
    """
    Fungsi untuk menghitung rata-rata nilai siswa dari list.
    Jika list kosong, kembalikan 0.
    """
    if len(nilai_siswa) == 0:
        print("List nilai kosong. Rata-rata tidak dapat dihitung.")
        return 0
    rata_rata = sum(nilai_siswa) / len(nilai_siswa)
    return rata_rata

# 4. Fungsi gabungkan_list: Gabungkan dua list tanpa duplikasi (menggunakan set untuk unique elements)
def gabungkan_list(list1, list2):
    """
    Fungsi untuk menggabungkan dua list menjadi satu list baru tanpa duplikasi.
    Menggunakan set untuk menghilangkan duplikat, lalu konversi kembali ke list.
    """
    list_gabungan = list(set(list1 + list2))  # + untuk konkatenasi, set untuk unique
    return list_gabungan

# 5. Fungsi cetak_daftar_siswa: Cetak nama dan nilai dari list dictionary
def cetak_daftar_siswa(daftar_siswa):
    """
    Fungsi untuk mencetak nama dan nilai setiap siswa dari list dictionary.
    Setiap dict berisi 'nama' dan 'nilai'.
    """
    if len(daftar_siswa) == 0:
        print("Daftar siswa kosong.")
        return
    
    print("Daftar Siswa:")
    print("-" * 30)
    for siswa in daftar_siswa:
        nama = siswa.get('nama', 'Tidak diketahui')
        nilai = siswa.get('nilai', 0)
        print(f"Nama: {nama}, Nilai: {nilai}")

# Bagian utama: Demonstrasi penggunaan semua fungsi
if __name__ == "__main__":
    print("=== Demonstrasi Project Python ===\n")
    
    # 1. Demonstrasi ubah_nilai (referensi objek)
    print("1. Demonstrasi Fungsi ubah_nilai (Referensi Objek):")
    list_asli = [10, 20, 30, 40]
    print(f"List asli sebelum perubahan: {list_asli}")
    ubah_nilai(list_asli)
    print(f"List asli setelah perubahan: {list_asli}\n")
    
    # 2. Demonstrasi perkenalan
    print("2. Demonstrasi Fungsi perkenalan:")
    perkenalan("Alice", 20)  # Dengan usia
    perkenalan("Bob")        # Tanpa usia (default 0)\n")
    
    # 3. Demonstrasi hitung_rata_rata
    print("3. Demonstrasi Fungsi hitung_rata_rata:")
    nilai1 = [80, 90, 70, 85]
    print(f"Nilai siswa: {nilai1}")
    print(f"Rata-rata: {hitung_rata_rata(nilai1)}")
    
    nilai_kosong = []
    print(f"Nilai kosong: {nilai_kosong}")
    print(f"Rata-rata: {hitung_rata_rata(nilai_kosong)}\n")
    
    # 4. Demonstrasi gabungkan_list
    print("4. Demonstrasi Fungsi gabungkan_list:")
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    hasil_gabung = gabungkan_list(list_a, list_b)
    print(f"List gabungan tanpa duplikasi: {hasil_gabung}\n")
    
    # 5. Demonstrasi cetak_daftar_siswa
    print("5. Demonstrasi Fungsi cetak_daftar_siswa:")
    daftar_siswa = [
        {'nama': 'Alice', 'nilai': 85},
        {'nama': 'Bob', 'nilai': 92},
        {'nama': 'Charlie', 'nilai': 78}
    ]
    cetak_daftar_siswa(daftar_siswa)
    
    daftar_kosong = []
    print("\n--- Daftar kosong ---")
    cetak_daftar_siswa(daftar_kosong)
    
    print("\n=== Akhir Demonstrasi ===")
