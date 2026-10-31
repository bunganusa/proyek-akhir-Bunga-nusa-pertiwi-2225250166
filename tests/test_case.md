# Dokumentasi Test Case Proyek

| ID Uji | Kategori | Input / Kondisi | Hasil yang Diharapkan | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | Nilai: 80, 70, 90 | Rata-rata 80.00 | Pass |
| **TC02** | Batas | Nilai: 0 | Diterima sebagai nilai valid | Pass |
| **TC03** | Batas | Nilai: 100 | Diterima sebagai nilai valid | Pass |
| **TC04** | Invalid | Nilai: 105 | Ditolak dengan pesan peringatan | Pass |
| **TC05** | Invalid | File data tidak ada | FileNotFoundError ditangani | Pass |
