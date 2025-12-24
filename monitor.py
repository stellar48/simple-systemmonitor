import psutil
import time
import os
from datetime import datetime
import wmi

# Trik ajaib untuk mengaktifkan fitur warna/posisi di Windows Terminal
os.system("")

def move_cursor_top():
    print("\033[H", end="")

# --- DEFINISI FUNGSI HARUS DI LUAR ---
# PENTING: Fungsi ini ditaruh di luar try/except agar selalu terbaca
def get_gpu_load_amd(wmi_obj):
    try:
        # PERBAIKAN TYPO: PerfFormattedData (bukan Performatted)
        data_mesin = wmi_obj.Win32_PerfFormattedData_GPUPerformanceCounters_GPUEngine()
        semua_load = [int(item.UtilizationPercentage) for item in data_mesin]
        if len(semua_load) > 0:
            return max(semua_load)
        else:
            return 0
    except:
        return 0

print("Mempersiapkan System Monitor (Versi Halus)...")
time.sleep(1)

# Bersihkan layar sekali saja di awal
os.system('cls' if os.name == 'nt' else 'clear')

print("Scanning GPU Hardware...")
c = wmi.WMI()

# Cek Nama GPU (Info Statis)
try:
    info_gpu = c.Win32_VideoController()[0]
    nama_gpu = info_gpu.Name
    driver_version = info_gpu.DriverVersion
except:
    nama_gpu = "GPU Standar"
    driver_version = "-"

# --- LOOP UTAMA (Harus sejajar di kiri, jangan masuk ke except) ---
try: 
    while True:
        move_cursor_top()
        
        # Ambil data
        cpu_pct = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        
        # GPU
        gpu_load = get_gpu_load_amd(c)

        # Logika Warna GPU
        if gpu_load > 50:
            warna_gpu = "\033[91m"
        else:
            warna_gpu = "\033[92m"

        RESET = "\033[0m"
        
        # Logika Warna CPU
        if cpu_pct > 50:
            warna_cpu = "\033[91m" # Merah bahaya
            status = "PANAS!"
        else:
            warna_cpu = "\033[92m" # Hijau aman
            status = "AMAN  "

        # --- TAMPILAN ---
        print("="*40 + " "*10)
        print("   SYSTEM MONITORING   ")
        print("="*40 + " "*10)
        
        # CPU
        print(f"CPU Usage : {warna_cpu}{cpu_pct}% ({status}){RESET}          ")
        bar_cpu = "|" * int(cpu_pct / 5) 
        print(f"Visual    : [{warna_cpu}{bar_cpu.ljust(20)}{RESET}]    ") 
        print("-" * 40 + " "*10)

        # GPU
        print(f"GPU Model : {nama_gpu}")
        print(f"GPU Load  : {warna_gpu}{gpu_load}%{RESET}          ")
        bar_gpu = "|" * int(gpu_load/5)
        print(f"Visual    : [{warna_gpu}{bar_gpu.ljust(20)}{RESET}]    ")
        print("-" * 40 + " "*10)

        # RAM
        used_gb = ram.used / (1024 ** 3)
        total_gb = ram.total / (1024 ** 3)
        print(f"RAM Usage : {ram.percent}%          ")
        print(f"Detail    : {used_gb:.2f} GB / {total_gb:.2f} GB      ")
        print("="*40 + " "*10)

        # --- FITUR LOGGING ---
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # PERBAIKAN CSV: Hapus label "CPU:", biar isinya cuma angka (bersih)
        data_log = f"{waktu},{cpu_pct},{ram.percent},{gpu_load}\n"
        
        with open("catatan_sistem.csv", "a") as file_log:
            file_log.write(data_log)
            
        print(f"STATUS    : [\033[91mREC\033[0m] Data tersimpan di catatan_sistem.csv  ")

except KeyboardInterrupt:
    print("\nProgram dihentikan.")