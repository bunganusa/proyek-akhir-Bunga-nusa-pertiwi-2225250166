import os
from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik
from utilitas import format_laporan

def main():
    print("=== Program Rekap & Analisis Nilai Matematika Kelas ===")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_data = os.path.join(base_dir, "data", "nilai_contoh.txt")
    path_output = os.path.join(base_dir, "output", "laporan_rekap.txt")
    KKM = 75.0
    
    try:
        print(f"\nMembaca data dari: {path_data}")
        data_mhs = baca_data(path_data)
        
        if not data_mhs:
            print("[Info] Tidak ada data nilai valid yang dapat diproses.")
            return

        statistik, detail_status = hitung_statistik(data_mhs, kkm=KKM)
        teks_laporan = format_laporan(statistik, detail_status)
        
        print("\n" + teks_laporan)
        
        if simpan_laporan(teks_laporan, path_output):
            print(f"\n[Sukses] Laporan berhasil disimpan ke: {path_output}")
        else:
            print("\n[Gagal] Laporan tidak dapat disimpan.")
            
    except FileNotFoundError as e:
        print(f"\n[Error] {e}")
    except Exception as e:
        print(f"\n[Error Tak Terduga] {e}")

if __name__ == "__main__":
    main()
