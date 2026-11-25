# 🎨 Blender Cloud Studio (Paduka Sambas)

Jalankan rendering 3D, animasi, dan script Python Blender langsung di **Cloud GitHub Actions** secara gratis tanpa membebani spek laptop/PC!

---

## 🚀 Fitur Utama

1. **Cloud Render Headless:** Blender versi Linux terbaru dijalankan di VM server GitHub.
2. **Support Python Scripting (`bpy`):** Buat model 3D, teks 3D, atau animasi langsung lewat script Python.
3. **Support File `.blend`:** Tinggal taruh file `.blend` Anda di folder `blend_files/` dan jalankan via tombol *Run workflow*.
4. **Auto Artifacts Download:** Hasil render (gambar PNG / video) otomatis bisa di-download di tab **Actions** > **Artifacts**.

---

## 🛠️ Cara Menggunakannya

### Opsi A: Jalankan Manual dari Browser
1. Buka tab **Actions** di repositori GitHub ini.
2. Pilih workflow **Blender Cloud Studio Runner** di sebelah kiri.
3. Klik tombol **Run workflow**.
4. (Opsional) Masukkan nama script atau file `.blend` yang ingin dirender serta resolusi (default: 1920x1080).
5. Klik **Run workflow** berwarna hijau.
6. Tunggu proses selesai (~1-2 menit), lalu download file **`blender-render-output`** di bagian bawah halaman run tersebut!

### Opsi B: Tambah File Anda Sendiri
- **Script Python:** Masukkan ke dalam folder `scripts/` (misal: `my_model.py`).
- **File Blender:** Masukkan ke dalam folder `blend_files/` (misal: `karakter.blend`).
- Lakukan Commit & Push, dan workflow siap merendernya di Cloud!

---
*Dibuat untuk Paduka Sambas Cloud Automation.*
