# Traveling Salesperson Problem (TSP) - Brute Force

Program Python sederhana untuk menyelesaikan *Traveling Salesperson Problem* (TSP) menggunakan algoritma Brute Force (pencarian ekskhaustif). 

Program ini mengevaluasi semua kemungkinan rute (permutasi) untuk menemukan jalur perjalanan terpendek yang mengunjungi setiap kota tepat satu kali dan kembali ke kota titik awal.

##  Alur dan Cara Kerja Program

Program ini dirancang dengan pendekatan *exhaustive search*, yang berarti ia akan mengevaluasi setiap kemungkinan secara paksa untuk menemukan hasil terbaik. Berikut adalah alur kerjanya:

1. **Inisialisasi Titik Awal:** Program menetapkan kota pertama (indeks `0`) sebagai titik keberangkatan dan titik akhir perjalanan secara permanen.
2. **Pemisahan Target Kunjungan:** Program memisahkan sisa kota lainnya (indeks `1` hingga `n-1`) ke dalam sebuah daftar target yang harus dikunjungi.
3. **Pembangkitan Permutasi:** Menggunakan fungsi `permutations` dari pustaka `itertools`, program menghasilkan semua kemungkinan kombinasi urutan kunjungan untuk kota-kota target tersebut.
4. **Kalkulasi Jarak Rute (Iterasi):** Untuk setiap urutan kombinasi yang dihasilkan, program melakukan simulasi perjalanan:
   * Dimulai dari kota `0`, lalu menjumlahkan jarak ke kota pertama dalam urutan.
   * Terus menjumlahkan jarak dari satu kota ke kota berikutnya secara berurutan.
   * Ditutup dengan menambahkan jarak dari kota terakhir untuk kembali pulang ke kota `0`.
5. **Evaluasi dan Pembaruan:** Setelah satu rute selesai dihitung, program membandingkan total jaraknya dengan rekor "jarak minimum" sementara. Jika rute saat ini terbukti lebih pendek, program akan langsung menimpa rekor jarak minimum dan memperbarui catatan "rute terbaik".
6. **Hasil Akhir:** Setelah semua ratusan atau ribuan kombinasi selesai dievaluasi, program akan mengembalikan rute yang dipastikan paling pendek beserta total beban jaraknya.

## Cara Menjalankan Program

Program ini murni menggunakan pustaka bawaan (*standard library*) sehingga tidak memerlukan instalasi *package* eksternal.

1. Simpan kode ke dalam sebuah file, misalnya `tsp_bruteforce.py`.
2. Buka terminal.
3. Eksekyut scriptmu :)
   ```bash
   python tsp_bruteforce.py
