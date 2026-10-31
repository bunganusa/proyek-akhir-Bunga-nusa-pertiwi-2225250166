def validasi_nilai(nilai: float) -> bool:
    return 0 <= nilai <= 100

def format_laporan(statistik: dict, daftar_status: list) -> str:
    laporan = []
    laporan.append("=" * 45)
    laporan.append("       LAPORAN REKAP DAN ANALISIS NILAI       ")
    laporan.append("=" * 45)
    laporan.append(f"Jumlah Siswa Valid : {statistik.get('total_siswa', 0)}")
    laporan.append(f"Rata-rata Nilai    : {statistik.get('rata_rata', 0.0):.2f}")
    laporan.append(f"Nilai Tertinggi    : {statistik.get('maksimum', 0.0):.2f}")
    laporan.append(f"Nilai Terendah     : {statistik.get('minimum', 0.0):.2f}")
    laporan.append(f"Jumlah Tuntas      : {statistik.get('jumlah_tuntas', 0)}")
    laporan.append(f"Jumlah Belum Tuntas: {statistik.get('jumlah_belum_tuntas', 0)}")
    laporan.append("-" * 45)
    laporan.append("DETAIL SISWA:")
    laporan.append(f"{'NIM/ID':<10} | {'Nama':<15} | {'Nilai':<6} | {'Status'}")
    laporan.append("-" * 45)
    
    for mhs in daftar_status:
        laporan.append(
            f"{mhs['id']:<10} | {mhs['nama']:<15} | {mhs['nilai']:<6.2f} | {mhs['status']}"
        )
    laporan.append("=" * 45)
    return "\n".join(laporan)
