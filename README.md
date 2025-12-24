# Simple System Monitor CLI (AMD Support)

Program pemantau sistem berbasis terminal (CLI) yang ringan, dibuat dengan Python.
Menampilkan penggunaan CPU, RAM, dan status GPU AMD secara real-time.

## Fitur
* **Real-time Monitoring**: CPU, RAM, dan GPU Load.
* **Visual Bar**: Grafik batang visual agar mudah dibaca.
* **Smart Alert**: Warna teks berubah (Hijau/Merah) berdasarkan suhu/beban.
* **Logging**: Menyimpan riwayat performa otomatis ke `catatan_sistem.csv`.
* **AMD Support**: Menggunakan WMI untuk mendeteksi GPU Radeon/Ryzen.

## Cara Menjalankan
1. Install dependencies:
   ```bash
   pip install psutil wmi
2. Menjalankan:
   ```bash
   python monitor.py

Requirements
Python 3.x
Windows OS
