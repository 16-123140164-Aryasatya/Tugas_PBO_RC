import tkinter as tk
from tkinter import messagebox, Menu
from datetime import datetime
import json
import os

# Nama file untuk simpan/load data
FILE_NAME = "catatan.json"
catatan_list = []

# Fungsi menyimpan catatan ke file JSON
def simpan_ke_file():
    with open(FILE_NAME, "w") as f:
        json.dump(catatan_list, f)

# Fungsi memuat catatan dari file JSON
def muat_dari_file():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            catatan_list.extend(data)
            for catatan in catatan_list:
                listbox_catatan.insert(tk.END, catatan["judul"])

# Fungsi tambah catatan
def tambah_catatan():
    judul = entry_judul.get().strip()
    isi = text_isi.get("1.0", tk.END).strip()
    if not judul or not isi:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    catatan = {"judul": f"{judul} ({waktu})", "isi": isi}
    catatan_list.append(catatan)
    listbox_catatan.insert(tk.END, catatan["judul"])
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

# Fungsi tampilkan isi catatan saat diklik
def tampilkan_catatan(event):
    selected = listbox_catatan.curselection()
    if selected:
        index = selected[0]
        isi = catatan_list[index]["isi"]
        text_isi.config(state="normal")  # aktifkan text area
        text_isi.delete("1.0", tk.END)
        text_isi.insert(tk.END, isi)

        entry_judul.delete(0, tk.END)
        judul_asli = catatan_list[index]["judul"].split(" (")[0]
        entry_judul.insert(0, judul_asli)

# Fungsi hapus catatan
def hapus_catatan():
    selected = listbox_catatan.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih catatan yang ingin dihapus!")
        return
    if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus catatan ini?"):
        index = selected[0]
        listbox_catatan.delete(index)
        catatan_list.pop(index)
        text_isi.config(state="normal")
        text_isi.delete("1.0", tk.END)
        entry_judul.delete(0, tk.END)

# Fungsi edit catatan
def edit_catatan():
    selected = listbox_catatan.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih catatan yang ingin diedit!")
        return
    judul_baru = entry_judul.get().strip()
    isi_baru = text_isi.get("1.0", tk.END).strip()
    if not judul_baru or not isi_baru:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    index = selected[0]
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    catatan_list[index] = {"judul": f"{judul_baru} ({waktu})", "isi": isi_baru}
    listbox_catatan.delete(index)
    listbox_catatan.insert(index, catatan_list[index]["judul"])
    listbox_catatan.select_set(index)  # Set kembali seleksi
    messagebox.showinfo("Sukses", "Catatan berhasil diperbarui!")

# Fungsi keluar aplikasi dan simpan otomatis
def keluar_aplikasi():
    simpan_ke_file()
    root.quit()

# Fungsi tampilkan dialog "Tentang"
def tampilkan_tentang():
    messagebox.showinfo("Tentang", "Catatan Harian v2.0\nDibuat dengan Python dan Tkinter")

# Inisialisasi GUI
root = tk.Tk()
root.title("Catatan Harian")

# Menu bar
menu_bar = Menu(root)
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Keluar", command=keluar_aplikasi)
menu_bar.add_cascade(label="File", menu=menu_file)

menu_bantuan = Menu(menu_bar, tearoff=0)
menu_bantuan.add_command(label="Tentang", command=tampilkan_tentang)
menu_bar.add_cascade(label="Bantuan", menu=menu_bantuan)
root.config(menu=menu_bar)

# Input judul
tk.Label(root, text="Judul:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_judul = tk.Entry(root, width=50)
entry_judul.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

# Tombol
tk.Button(root, text="Tambah Catatan", command=tambah_catatan).grid(row=1, column=1, sticky="e", padx=5)
tk.Button(root, text="Hapus Catatan", command=hapus_catatan).grid(row=1, column=2, sticky="w", padx=5)
tk.Button(root, text="Edit Catatan", command=edit_catatan).grid(row=1, column=0, sticky="w", padx=5)

# Listbox + scrollbar
listbox_catatan = tk.Listbox(root, width=30, height=10)
listbox_catatan.grid(row=2, column=0, rowspan=3, padx=5, pady=5, sticky="ns")
listbox_catatan.bind("<<ListboxSelect>>", tampilkan_catatan)

scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox_catatan.yview)
scrollbar.grid(row=2, column=1, sticky="nsw", rowspan=3)
listbox_catatan.config(yscrollcommand=scrollbar.set)

# Area isi catatan
text_isi = tk.Text(root, width=40, height=10)
text_isi.grid(row=2, column=2, rowspan=3, padx=5, pady=5, sticky="nsew")

# Layout fleksibel
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)

# Muat data dari file saat aplikasi dibuka
muat_dari_file()

# Jalankan aplikasi
root.mainloop()
