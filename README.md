# Web Scraping Kompas.com Articles

<p align="center">
  <img src="https://algorit.ma/wp-content/uploads/2023/02/LOGO-KOMPAS.COM-WARNA-01-2-300x74.png" alt="Kompas Logo" width="500">
</p>

Kompas.com adalah salah satu portal berita terkemuka di Indonesia yang menyediakan berita terkini dan terpercaya dari berbagai bidang, termasuk politik, ekonomi, olahraga, teknologi, hiburan, dan lainnya. 
Situs ini dikenal karena kualitas jurnalistiknya yang tinggi dan cakupan berita yang luas, mencakup berita nasional dan internasional. 
Kompas.com juga menawarkan berbagai fitur tambahan seperti opini, analisis, video berita, dan infografis untuk memberikan informasi yang komprehensif kepada pembacanya. 
Dengan penyajian yang cepat dan akurat, Kompas.com menjadi sumber informasi utama bagi masyarakat Indonesia.

Proyek ini bertujuan untuk melakukan web scraping artikel terkait "Jakarta" atau bisa dengan wilayah lain tapi disini saya akan mengambil wilayah Jakarta. 
dari halaman web Kompas menggunakan Python dengan modul BeautifulSoup, requests, pandas dan lain-lain.

## Persyaratan

Instalasi modul yang diperlukan:
- 'datetime'
- 'tabulate'
- 'pandas'
- 'json'
- 'BeautifulSoup'
- 'Counter'
- 're'
- 'requests'

Anda dapat menginstal modul-modul tersebut menggunakan pip.

## Cara Penggunaan

1. **Mengimpor Modul yang Diperlukan**: Impor modul BeautifulSoup, requests, dan pandas di dalam script Python Anda.

2. **Mengambil Konten Halaman Web**: Gunakan requests untuk mengambil konten halaman web dari URL yang diinginkan.

3. **Mem-parsing Konten HTML**: Gunakan BeautifulSoup untuk mem-parsing konten HTML yang telah diambil.

4. **Menemukan dan Mengambil Data yang Diinginkan**: Tentukan elemen-elemen HTML yang berisi data yang Anda ingin ambil, seperti judul artikel, ringkasan, tautan, dan tanggal.

5. **Menyimpan Data ke dalam DataFrame pandas**: Buat DataFrame pandas untuk menyimpan data yang telah diambil.

6. **Menyimpan Data ke File CSV**: Simpan DataFrame ke dalam file CSV untuk analisis lebih lanjut.

## Kode Lengkap

Lihat contoh kode lengkap di dalam script Python untuk implementasi lebih rinci.
