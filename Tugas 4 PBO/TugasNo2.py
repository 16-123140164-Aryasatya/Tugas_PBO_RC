class error(Exception): # Jika terjadi kesalahan dalam daftar
    """Exception khusus untuk kesalahan dalam daftar tugas."""
    pass

def menu(): # menampilkan menu
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah(daftar): # Menambahkan tugas
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise error("Tugas tidak boleh kosong.")
    
    daftar.append(tugas) # tugas ditambahkan
    print("Tugas berhasil ditambahkan!")

def hapus(daftar): # Menghapusdaftar tugas
    if not daftar:
        raise error("Tidak ada tugas yang bisa dihapus.")
    
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(daftar):
            raise IndexError
        
        dihapus = daftar.pop(nomor - 1) # Menghapus tugas
        print(f"Tugas '{dihapus}' berhasil dihapus!")
    except ValueError:
        raise error("Masukkan angka yang valid.")
    except IndexError:
        raise error(f"Tugas dengan nomor {nomor} tidak ditemukan.")

def tampilkan(daftar): # Menampilkan daftar tugas
    if not daftar:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for i, tugas in enumerate(daftar, 1):
            print(f"{i}. {tugas}")

def main():
    daftar = []
    
    while True: # Perulangan
        menu()
        try:
            pil = int(input("Masukkan pilihan (1/2/3/4): "))
            
            if pil == 1:
                try:
                    tambah(daftar)
                except error as e:
                    print(f"Error: {e}")
            elif pil == 2:
                try:
                    hapus(daftar)
                except error as e:
                    print(f"Error: {e}")
            elif pil == 3:
                tampilkan(daftar)
            elif pil == 4:
                print("Keluar dari program.")
                break
            else:
                print("Error: Pilihan tidak valid. Masukkan angka 1-4.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
