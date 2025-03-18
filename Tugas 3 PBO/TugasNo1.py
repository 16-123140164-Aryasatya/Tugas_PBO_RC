class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)
        
    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)
        
    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)
        
    def __truediv__(self, other):
        if other.nilai != 0:
            return Kalkulator(self.nilai / other.nilai)
        else:
            raise ValueError("Cannot divide by zero")
    
    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)
        
    def log(self):
        if self.nilai > 0:
            result = 0
            n = self.nilai - 1
            for i in range(1, 20):
                term = ((-1) ** (i + 1)) * (n ** i) / i
                result += term
            return Kalkulator(result)
        else:
            raise ValueError("Logarithm undefined for non-positive values")    
       
    def __str__(self):
        return f"Result: {self.nilai}"

# Input dari pengguna
nilai1 = float(input("Masukkan angka pertama: "))
nilai2 = float(input("Masukkan angka kedua: "))

angka1 = Kalkulator(nilai1)
angka2 = Kalkulator(nilai2)

print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pangkat:", angka1 ** angka2)
print("Logaritma angka pertama:", angka1.log())