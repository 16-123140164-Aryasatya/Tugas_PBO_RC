#Aryasatya Widyatna Akbar
#123140164
#Tugas Praktikum PBO RC

# No 1
height = int(input("Masukkan tinggi segitiga: "))
print(f"Height: {height}")
for i in range(1, height + 1):
    spasi = " " * (height - i)  
    bintang = "*" * (2 * i - 1)   
    print(spasi + bintang)

# No 2
data = {}

jumlah = int(input("Masukkan jumlah siswa: "))

for i in range(1, jumlah + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ")  
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))  
    data[nama] = nilai  

print("\ndictionary =", data)


