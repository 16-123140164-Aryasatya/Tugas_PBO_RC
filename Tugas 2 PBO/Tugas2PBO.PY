import random 

class Robot:
    def __init__(self, nama, attack, hp, accuracy):
        self.nama = nama
        self.attack = attack
        self.hp = hp
        self.accuracy = accuracy
        self.stun = False  # Status stun default
    
    def serang(self, musuh): # Funsi untuk menyerang
        if random.random() <= self.accuracy:  # Menentukan keberhasilan serangan
            damage = self.attack
            musuh.hp -= damage
            print(f"{self.nama} menyerang {musuh.nama} dan memberikan {damage} damage!")
        else:
            print(f"{self.nama} mencoba menyerang {musuh.nama} tetapi meleset!")
    
    def regen(self): # Fungsi untuk memulihkan hp
        heal = random.randint(5, 15)
        self.hp += heal
        print(f"{self.nama} meregenerasi HP sebanyak {heal}. HP saat ini: {self.hp}")
    
    def skill(self, musuh): # Fungsi untuk menggunakan stun
        if random.random() < 0.3:  # 30% kemungkinan menggunakan stun
            print(f"{self.nama} menggunakan skill Stun pada {musuh.nama}!")
            musuh.stun = True  # Status stun aktif pada musuh
        else:
            self.serang(musuh)  # Tetap menyerang walaupun tidak menggunakan skill
    
    def alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2, ronde, singleplayer=False):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = ronde
        self.singleplayer = singleplayer
    
    def start(self):
        print("--- FIGHT!!! ---")
        for rondes in range(1, self.ronde + 1):
            print(f"\n--- Ronde {rondes} ---")
            
            if not self.robot1.alive() or not self.robot2.alive():
                break
            
            # Giliran Player 1
            if not self.robot1.stun:
                print(f"Giliran {self.robot1.nama}")
                action = input(f"{self.robot1.nama}, pilih aksi: (1) Serang (2) Regenerasi HP: ")
                if action == "1":
                    self.robot1.skill(self.robot2)
                elif action == "2":
                    self.robot1.regen()
            else:
                print(f"{self.robot1.nama} sedang stun dan tidak bisa bergerak!")
                self.robot1.stun = False  # Hilangkan stun setelah 1 ronde
            
            if not self.robot2.alive():
                print(f"{self.robot2.nama} telah kalah! {self.robot1.nama} menang!")
                break
            
            # Giliran Player 2
            if not self.robot2.stun:
                print(f"Giliran {self.robot2.nama}")
                if self.singleplayer:  # Bot akan memilih tindakan secara acak
                    action = random.choice(["1", "2"])
                else:
                    action = input(f"{self.robot2.nama}, pilih aksi: (1) Serang (2) Regenerasi HP: ")
                
                if action == "1":
                    self.robot2.skill(self.robot1)
                elif action == "2":
                    self.robot2.regen()
            else:
                print(f"{self.robot2.nama} sedang stun dan tidak bisa bergerak!")
                self.robot2.stun = False  # Hilangkan stun setelah 1 ronde
            
            print(f"{self.robot1.nama} HP: {self.robot1.hp} | {self.robot2.nama} HP: {self.robot2.hp}")
            
            if not self.robot1.alive():
                print(f"{self.robot1.nama} telah kalah! {self.robot2.nama} menang!")
                break
        else:
            print("Pertarungan berakhir tanpa pemenang!")

# Pemilihan Mode
mode = input("Pilih mode permainan: (1) Singleplayer (2) Multiplayer: ")

nama1 = input("Masukkan nama robot pertama: ")
robot1 = Robot(nama1, attack=15, hp=100, accuracy=0.9)

if mode == "1":
    robot2 = Robot("Bot", attack=15, hp=100, accuracy=0.9)
    game = Game(robot1, robot2, ronde=100, singleplayer=True)
else:
    nama2 = input("Masukkan nama robot kedua: ")
    robot2 = Robot(nama2, attack=15, hp=100, accuracy=0.9)
    game = Game(robot1, robot2, ronde=100, singleplayer=False)

game.start()