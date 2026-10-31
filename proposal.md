# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Terminal.

## 2. Latar Belakang
Guru matematika sering mengalokasikan waktu cukup banyak untuk merekapitulasi nilai secara manual, menghitung statistik kelas, dan menentukan ketuntasan siswa. Program ini dibuat untuk mempermudah dan mempercepat proses olah nilai secara otomatis, akurat, serta konsisten.

## 3. Pengguna dan Tujuan
- **Pengguna**: Guru / Pendidik Matematika.
- **Tujuan**: Membaca data nilai dari berkas, memvalidasi input, menghitung nilai rata-rata, minimum, maksimum, serta menentukan status ketuntasan siswa berdasarkan nilai KKM.

## 4. Ruang Lingkup
- Aplikasi berbasis terminal / console (Python).
- Memproses data dari berkas teks format terstruktur.
- Menganalisis nilai pada rentang valid 0–100.
- Menghasilkan ringkasan laporan berbasis teks.

## 5. Kebutuhan Sistem
### Kebutuhan Fungsional (Wajib)
- **F01**: Membaca data nilai siswa dari file teks.
- **F02**: Memvalidasi input nilai (rentang 0–100).
- **F03**: Menghitung rata-rata, nilai minimum, dan nilai maksimum.
- **F04**: Menentukan status ketuntasan berdasarkan KKM.
- **F05**: Menyimpan laporan hasil rekap ke berkas teks output.

### Kebutuhan Non-Fungsional
- Eksekusi program ringan dan responsif pada terminal VS Code.
- Penanganan error terstruktur saat berkas tidak ditemukan atau format tidak sesuai.

## 6. Input, Proses, dan Output (IPO)
- **Input**: Berkas `data/nilai_contoh.txt` berisi baris `(ID, Nama, Nilai)`.
- **Proses**: Read file → Validasi nilai → Hitung statistik → Klasifikasi ketuntasan (KKM = 75).
- **Output**: Tampilan ringkasan statistik pada terminal dan berkas `output/laporan_rekap.txt`.

## 7. Algoritma (Pseudocode)
```text
MULAI
    BACA path_file
    JIKA file tidak ada:
        TAMPILKAN "File tidak ditemukan"
        SELESAI

    UNTUK SETIAP baris DALAM file:
        AMBIL id, nama, nilai
        JIKA 0 <= nilai <= 100:
            SIMPAN ke daftar_valid
        LAINNYA:
            TAMPILKAN pesan peringatan

    JIKA daftar_valid KOSONG:
        TAMPILKAN "Tidak ada data valid"
        SELESAI

    HITUNG statistik (rata-rata, min, max, ketuntasan)
    TAMPILKAN laporan ke layar
    SIMPAN laporan ke file output
SELESAI