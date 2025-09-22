siswa = []

def tambah_siswa(nama, nilai):
    if not isinstance(nilai, (int, float)) or nilai < 0 or nilai > 100:
        print(f"Error: Nilai {nilai} tidak valid. Harus berupa angka 0-100.")
        return
    siswa.append({"nama": nama, "nilai": int(nilai)})  
    print(f"Siswa {nama} dengan nilai {nilai} berhasil ditambahkan.")

def hapus_siswa(nama):
    for i, s in enumerate(siswa):
        if s["nama"].lower() == nama.lower():  
            siswa.pop(i)  
            print(f"Siswa {nama} telah dihapus.")
            return
    print(f"Siswa {nama} tidak ditemukan.")

def hitung_rata_rata():
    if len(siswa) == 0:
        print("List siswa kosong. Rata-rata tidak dapat dihitung.")
        return None
    total_nilai = sum(s["nilai"] for s in siswa)
    rata_rata = total_nilai / len(siswa)
    return rata_rata

def cetak_daftar_siswa():
    if len(siswa) == 0:
        print("Daftar siswa kosong.")
        return
    print("Daftar Siswa:")
    print("-" * 30)
    for s in siswa:
        print(f"Nama: {s['nama']}, Nilai: {s['nilai']}")

# Fungsi urutkan_siswa() yang DIPISAHKAN dan DIDEFINISIKAN SECARA TERpisAH
def urutkan_siswa():
    if len(siswa) == 0:
        print("List siswa kosong. Tidak bisa diurutkan.")
        return
    siswa.sort(key=lambda x: x["nilai"])
    print("Siswa telah diurutkan berdasarkan nilai (ascending).")

def cari_siswa(nama):
    for s in siswa:
        if s["nama"].lower() == nama.lower():
            print(f"Siswa ditemukan: Nama: {s['nama']}, Nilai: {s['nilai']}")
            return
    print(f"Siswa {nama} tidak ditemukan.")

def menu_utama():
    while True:
        print("\n=== Menu Manajemen Siswa ===")
        print("1. Tambah Siswa")
        print("2. Hapus Siswa")
        print("3. Cetak Daftar Siswa")
        print("4. Hitung Rata-Rata Nilai")
        print("5. Urutkan Siswa Berdasarkan Nilai")
        print("6. Cari Siswa")
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ").strip()
        
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ").strip()
            try:
                nilai = float(input("Masukkan nilai (0-100): "))
                tambah_siswa(nama, nilai)
            except ValueError:
                print("Error: Nilai harus berupa angka.")
        
        elif pilihan == "2":
            nama = input("Masukkan nama siswa yang akan dihapus: ").strip()
            hapus_siswa(nama)
        
        elif pilihan == "3":
            cetak_daftar_siswa()
        
        elif pilihan == "4":
            rata_rata = hitung_rata_rata()
            if rata_rata is not None:
                print(f"Rata-rata nilai: {rata_rata:.2f}")
        
        elif pilihan == "5":
            urutkan_siswa()
            cetak_daftar_siswa()  # Cetak ulang setelah diurutkan untuk melihat hasil
        
        elif pilihan == "6":
            nama = input("Masukkan nama siswa yang dicari: ").strip()
            cari_siswa(nama)
        
        elif pilihan == "7":
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    print("=== Demonstrasi Awal (seperti kode asli) ===")
    
    tambah_siswa("Budi", 85)
    tambah_siswa("Sari", 90)
    tambah_siswa("Andi", 78)
    
    cetak_daftar_siswa()
    rata_rata = hitung_rata_rata()
    if rata_rata is not None:
        print(f"Rata-rata nilai: {rata_rata:.2f}")
    
    hapus_siswa("Andi")
    cetak_daftar_siswa()
    urutkan_siswa()  # Sekarang ini tidak error
    cetak_daftar_siswa()
    print("\n=== Demonstrasi Selesai. Mulai Menu Interaktif ===")
    menu_utama()
