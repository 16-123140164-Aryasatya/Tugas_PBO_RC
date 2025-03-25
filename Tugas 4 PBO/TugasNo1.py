def hitung_akar():
    while True:
        try:
            angka = float(input("Masukkan angka: "))

            # Mengecek apakah angka negatif
            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
                continue  

            # Mengecek apakah angka nol
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
                continue  

            # Jika angka valid, hitung akar kuadratnya
            akar = angka ** 0.5
            print(f"Akar kuadrat dari {angka} adalah {akar:.1f}")
            break  # Keluar dari loop jika input valid

        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

# Menjalankan program
hitung_akar()
