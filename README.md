# 📊 Program Rekap dan Analisis Nilai Matematika Kelas

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-In%20Development-orange)

Aplikasi berbasis antarmuka baris perintah (*command-line interface* / CLI) menggunakan Python untuk membantu guru matematika mengolah data nilai siswa secara otomatis, akurat, dan konsisten. Program ini dirancang untuk memenuhi Tugas Proyek Akhir Mata Kuliah **Algoritma dan Pemrograman** (S1 Pendidikan Matematika FKIP UNTIRTA).

---

## 📌 Fitur Utama

- 📂 **Membaca Data Otomatis**: Membaca file `.txt` yang berisi ID, Nama, dan Nilai siswa.
- 🛡️ **Validasi Input Rigor**: Memastikan nilai berada pada rentang valid $0 \le \text{nilai} \le 100$ dan mengabaikan format data yang rusak (*corrupted*).
- 📈 **Analisis Statistik Kelas**:
  - Menghitung nilai rata-rata kelas.
  - Menentukan nilai tertinggi (maksimum) dan terendah (minimum).
- 🎯 **Klasifikasi Ketuntasan (KKM)**: Menghitung jumlah siswa yang tuntas dan belum tuntas berdasarkan nilai KKM (default: 75.0).
- 📝 **Ekspor Laporan**: Mencetak ringkasan hasil rekap ke terminal dan menyimpannya secara otomatis ke file `output/laporan_rekap.txt`.

---

## 📂 Struktur Repositori

```text
proyek-akhir-nama-tim/
├── .gitignore
├── README.md
├── proposal.md
├── data/
│   └── nilai_contoh.txt      # Data sampel input nilai
├── output/
│   ├── .gitkeep              # Penanda repositori Git
│   └── laporan_rekap.txt     # Hasil output eksekusi program
├── src/
│   ├── __init__.py
│   ├── analisis.py           # Logika matematika & kalkulasi statistik
│   ├── data_io.py            # Pemrosesan baca/tulis file (I/O)
│   ├── main.py               # Main entry point program
│   └── utilitas.py           # Fungsi validasi & pemformatan laporan
└── tests/
    └── test_case.md          # Rincian skenario pengujian (Normal, Batas, Invalid)
