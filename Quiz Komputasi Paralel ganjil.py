import multiprocessing
import time
import os

# --- IMPLEMENTASI TASK PARALLELISM PADA SISTEM IOT CERDAS ---

def modul_pengolah_citra():
    """Tugas 1: Menganalisis video feed untuk deteksi pelanggaran"""
    pid = os.getpid()
    print(f"[CAM-ANALYSIS - PID {pid}] Menganalisis frame video dari kamera utama...")
    time.sleep(3.7) # Simulasi beban komputasi image processing
    print(f"[CAM-ANALYSIS] SELESAI: Tidak ada foul terdeteksi.")

def modul_sensor_ring():
    """Tugas 2: Deteksi bola masuk menggunakan sensor infra merah"""
    pid = os.getpid()
    print(f"[RING-SENSOR - PID {pid}] Siaga memantau getaran dan sensor IR pada ring...")
    time.sleep(1.8)
    print(f"[RING-SENSOR] SELESAI: Bola masuk terdeteksi, skor +3.")

def modul_pelacak_pemain():
    """Tugas 3: Sinkronisasi data posisi GPS pemain di lapangan"""
    pid = os.getpid()
    print(f"[GPS-TRACKER - PID {pid}] Mengupdate koordinat heatmap pemain...")
    time.sleep(2.5)
    print(f"[GPS-TRACKER] SELESAI: Data posisi berhasil dikirim ke database.")

def modul_shot_clock():
    """Tugas 4: Manajemen waktu shot clock 24 detik"""
    pid = os.getpid()
    print(f"[TIMER-SYS - PID {pid}] Mengatur sinkronisasi waktu shot clock...")
    time.sleep(1.2)
    print(f"[TIMER-SYS] SELESAI: Waktu sinkron dengan buzzer utama.")

def modul_api_broadcast():
    """Tugas 5: Mengirim data ke API untuk tampilan live score di web"""
    pid = os.getpid()
    print(f"[API-GATEWAY - PID {pid}] Push data statistik ke server cloud...")
    time.sleep(2.0)
    print(f"[API-GATEWAY] SELESAI: Live score di website Itenas berhasil diupdate.")

def modul_log_system():
    """Tugas 6: Mencatat log aktivitas sistem ke dalam file lokal"""
    pid = os.getpid()
    print(f"[SYS-LOGGER - PID {pid}] Mencatat log aktivitas sistem ke server...")
    time.sleep(1.5)
    print(f"[SYS-LOGGER] SELESAI: Log aktivitas berhasil disimpan.")

if __name__ == "__main__":
    print("="*65)
    print("IMPLEMENTASI TASK PARALLELISM: SMART BASKETBALL COURT IOT")
    print(f"Main Process ID: {os.getpid()}")
    print("="*65)
    
    start_execution = time.time()

    # Inisialisasi proses paralel untuk setiap modul sensor yang berbeda
    tugas_paralel = [
        multiprocessing.Process(target=modul_pengolah_citra),
        multiprocessing.Process(target=modul_sensor_ring),
        multiprocessing.Process(target=modul_pelacak_pemain),
        multiprocessing.Process(target=modul_shot_clock),
        multiprocessing.Process(target=modul_api_broadcast),
        multiprocessing.Process(target=modul_log_system)
    ]

    # Menjalankan seluruh modul secara serentak (Parallel)
    for t in tugas_paralel:
        t.start()

    # Menunggu seluruh modul menyelesaikan tugasnya
    for t in tugas_paralel:
        t.join()

    end_execution = time.time()
    
    print("="*65)
    print(f"TOTAL DURASI EKSEKUSI PARALEL: {round(end_execution - start_execution, 2)} DETIK")
    print("="*65)