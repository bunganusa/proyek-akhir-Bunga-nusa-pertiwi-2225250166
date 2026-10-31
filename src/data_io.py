import os
from utilitas import validasi_nilai

def baca_data(path_file: str) -> list:
    if not os.path.exists(path_file):
        raise FileNotFoundError(f"File data '{path_file}' tidak ditemukan.")

    data_mahasiswa = []
    with open(path_file, 'r', encoding='utf-8') as file:
        for baris_ke, baris in enumerate(file, 1):
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            
            pemisah = ',' if ',' in baris else ';'
            bagian = baris.split(pemisah)
            
            if len(bagian) < 3:
                print(f"[Peringatan] Baris {baris_ke} diabaikan: Format kurang dari 3 kolom.")
                continue
            
            mhs_id = bagian[0].strip()
            nama = bagian[1].strip()
            
            try:
                nilai = float(bagian[2].strip())
            except ValueError:
                print(f"[Peringatan] Baris {baris_ke} diabaikan: Nilai '{bagian[2]}' bukan angka.")
                continue
            
            if validasi_nilai(nilai):
                data_mahasiswa.append({
                    "id": mhs_id,
                    "nama": nama,
                    "nilai": nilai
                })
            else:
                print(f"[Peringatan] Baris {baris_ke} diabaikan: Nilai {nilai} di luar rentang (0-100).")
                
    return data_mahasiswa

def simpan_laporan(isi_laporan: str, path_output: str) -> bool:
    try:
        os.makedirs(os.path.dirname(path_output), exist_ok=True)
        with open(path_output, 'w', encoding='utf-8') as file:
            file.write(isi_laporan)
        return True
    except Exception as e:
        print(f"[Error] Gagal menyimpan laporan: {e}")
        return False
