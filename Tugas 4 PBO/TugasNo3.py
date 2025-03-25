# Kelas dasar
class hewan:
    """Kelas dasar sebagai blueprint untuk hewan di kebun binatang."""
    
    def __init__(self, nama, umur):
        if not nama.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        if not isinstance(umur, int) or umur <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        
        self.__nama = nama
        self.__umur = umur
    
    # Getter
    def get_nama(self):
        return self.__nama
    
    def get_umur(self):
        return self.__umur
    
    # Setter
    def set_nama(self, nama):
        if not nama.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        self.__nama = nama
    
    def set_umur(self, umur):
        if not isinstance(umur, int) or umur <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        self.__umur = umur
    
    # Method abstrak
    def reproduksi(self):
        """Method ini akan dioverride di subclass."""
        return "Reproduksi hewan tidak diketahui"
    
    def info(self):
        """Menampilkan informasi umum tentang hewan."""
        return f"{self.__nama} berusia {self.__umur} tahun."

# Subclass berdasarkan kategori hewan
class Aves(hewan):  # Burung
    def reproduksi(self):
        return "Ovipar! 🐦"

class Mammal(hewan):  # Mamalia
    def reproduksi(self):
        return "Vivipar! 🐻"

class Reptile(hewan):  # Reptil
    def reproduksi(self):
        return "Ovipar, Vivipar, Ovovivipar! 🐍"

class Pisces(hewan):  # Ikan
    def reproduksi(self):
        return "Ovipar, Vivipar, Ovovivipar! 🐠"

class Amphibian(hewan):  # Amphibi
    def reproduksi(self):
        return "Ovipar, Vivipar 🐸"

# Program Utama
def main():
    zoo = []  # List untuk menyimpan objek hewan
    
    while True:
        print("\n===== Sistem Manajemen Hewan di Kebun Binatang =====")
        print("1. Tambah Hewan")
        print("2. Tampilkan Semua Hewan")
        print("3. Keluar")
        
        try:
            pil = int(input("Masukkan pilihan (1/2/3): "))
            
            if pil == 1:
                print("\nKategori Hewan:")
                print("1. Aves (Burung) 🐦")
                print("2. Mamalia 🐻")
                print("3. Reptil 🐍")
                print("4. Pisces (Ikan) 🐠")
                print("5. Amphibi 🐸")
                
                jenis = int(input("Pilih kategori hewan (1-5): "))
                nama = input("Masukkan nama hewan: ").strip()
                usia = int(input("Masukkan usia hewan: "))
                
                if jenis == 1:
                    hewan = Aves(nama, usia)
                elif jenis == 2:
                    hewan = Mammal(nama, usia)
                elif jenis == 3:
                    hewan = Reptile(nama, usia)
                elif jenis == 4:
                    hewan = Pisces(nama, usia)
                elif jenis == 5:
                    hewan = Amphibian(nama, usia)
                else:
                    print("Error: Pilihan kategori tidak valid.")
                    continue
                
                zoo.append(hewan)
                print(f"{nama} berhasil ditambahkan ke kebun binatang! 🎉")
            
            elif pil == 2:
                if not zoo:
                    print("Belum ada hewan di kebun binatang.")
                else:
                    print("\n=== Daftar Hewan di Kebun Binatang ===")
                    for index, hewan in enumerate(zoo, 1):
                        print(f"{index}. {hewan.info()} - reproduksi: {hewan.reproduksi()}")
            
            elif pil == 3:
                print("Keluar dari program. Sampai jumpa! 👋")
                break
            
            else:
                print("Error: Pilihan tidak valid. Masukkan angka 1-3.")
        
        except ValueError as e:
            print(f"Error: {e}. Masukkan input yang sesuai.")

if __name__ == "__main__":
    main()
