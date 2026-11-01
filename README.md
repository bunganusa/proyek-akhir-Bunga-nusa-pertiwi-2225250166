# Program Rekap dan Analisis Nilai Matematika Kelas

**Mata Kuliah:** Algoritma dan Pemrograman (Pertemuan 14 & 15)  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.  

---

## 1. Deskripsi
Program ini dikembangkan untuk membantu guru matematika mengolah rekapitulasi nilai siswa secara otomatis dari file teks. Program memvalidasi rentang nilai (0–100), menghitung nilai rata-rata, nilai minimum, nilai maksimum, menentukan status ketuntasan berdasarkan KKM, serta mengekspor hasil statistik ke dalam file laporan.

---

## 2. Fitur Utama
- **Membaca File Data:** Memuat data ID, Nama, dan Nilai dari file `.txt` yang berada di folder `data/`.
- **Validasi Nilai Ketat:** Menyaring nilai di luar rentang 0 - 100 dan menangani format baris yang tidak sesuai.
- **Analisis Statistik:** Perhitungan otomatis untuk nilai rata-rata, nilai tertinggi (max), dan nilai terendah (min).
- **Analisis Ketuntasan KKM:** Klasifikasi siswa tuntas ($\ge 75$) dan belum tuntas.
- **Ekspor Laporan:** Menyimpan ringkasan rekapitulasi secara otomatis ke folder `output/laporan_rekap.txt`.

---

## 3. Struktur Folder Proyek
```text
proyek-akhir-nama-tim/
├── .gitignore
├── README.md
├── proposal.md
├── data/
│   └── nilai_contoh.txt      # File data nilai input
├── output/
│   ├── .gitkeep              # Penanda folder Git
│   └── laporan_rekap.txt     # File hasil ekspor laporan
├── src/
│   ├── __init__.py
│   ├── analisis.py           # Logika kalkulasi & statistik
│   ├── data_io.py            # Pemrosesan baca/tulis file (I/O)
│   ├── main.py               # Main entry point program
│   └── utilitas.py           # Validasi nilai & format laporan
└── tests/
    └── test_case.md          # Dokumen skenario uji coba