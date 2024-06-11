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

## Output

Output dari skrip ini mencakup dua format utama: DataFrame pandas dan JSON.

1. **DataFrame Pandas**: Ini adalah struktur data yang digunakan dalam Python untuk menganalisis dan memanipulasi data tabular. Dalam konteks ini, DataFrame digunakan untuk menyimpan informasi yang di-scrape dari Kompas.com. Setiap baris DataFrame mewakili satu artikel berita dan kolomnya berisi informasi seperti:
   - Tanggal scraping: Waktu ketika scraping dilakukan.
   - Nama portal berita: Nama portal berita (dalam hal ini, "kompas_com").
   - Tanggal rilis berita: Tanggal rilis dari berita.
   - Judul Berita: Judul dari berita.
   - URL Berita: URL lengkap dari berita.
   - Kata sering muncul: Kata-kata yang sering muncul dalam berita setelah mengabaikan kata-kata yang umum.

   Informasi ini diorganisir dalam bentuk tabel yang memudahkan untuk ditampilkan dan dianalisis.

2. **JSON (JavaScript Object Notation)**: Ini adalah format data yang digunakan untuk pertukaran data yang ringan dan mudah dibaca oleh manusia. Output JSON dari skrip ini berisi array objek, di mana setiap objek mewakili satu artikel berita dan memiliki properti seperti:
   - Tanggal scraping
   - Nama portal berita
   - Tanggal rilis berita
   - Judul Berita
   - URL Berita
   - Kata sering muncul

   Informasi ini diorganisir dalam format yang mudah dibaca oleh mesin dan dapat dengan mudah diproses oleh aplikasi lain yang memerlukan data tersebut.

Dengan menggunakan DataFrame pandas dan JSON, informasi yang di-scrape dari Kompas.com dapat disimpan, diakses, dan dianalisis lebih lanjut sesuai kebutuhan pengguna.

## Kode Lengkap

Lihat contoh kode lengkap di dalam script Python untuk implementasi lebih rinci.
