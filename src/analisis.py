def tentukan_status(nilai: float, kkm: float = 75.0) -> str:
    if nilai >= kkm:
        return "TUNTAS"
    return "BELUM TUNTAS"

def hitung_statistik(data_mahasiswa: list, kkm: float = 75.0) -> tuple:
    if not data_mahasiswa:
        return {}, []

    semua_nilai = [mhs["nilai"] for mhs in data_mahasiswa]
    total_siswa = len(semua_nilai)
    rata_rata = sum(semua_nilai) / total_siswa
    maksimum = max(semua_nilai)
    minimum = min(semua_nilai)
    
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0
    data_dengan_status = []

    for mhs in data_mahasiswa:
        status = tentukan_status(mhs["nilai"], kkm)
        if status == "TUNTAS":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1
            
        mhs_copy = mhs.copy()
        mhs_copy["status"] = status
        data_dengan_status.append(mhs_copy)

    statistik = {
        "total_siswa": total_siswa,
        "rata_rata": rata_rata,
        "maksimum": maksimum,
        "minimum": minimum,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas
    }

    return statistik, data_dengan_status
