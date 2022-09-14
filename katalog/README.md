# Tugas 2 PBP
Link aplikasi : [Link Aplikasi](https://newappmvt.herokuapp.com/katalog/) 

## User Request
![Bagan Request](https://github.com/kayleerudaina/files/blob/main/bagantugas2.png?raw=true)

## Mengapa Virtual Environment dipakai di Django?
Virtual Environment merupakan sebuah tool yang dipakai untuk menyimpan _dependencies_ yang diperlukan. _Dependencies_ yang diperlukan oleh suatu aplikasi berbeda-beda dan bisa berubah ketika kita _upgrade_ ke versi baru atau melakukan perubahan lainnya kepada aplikasi. Dengan Virtual Environment, kita akan membuat suatu 'ruang' yang terisolalsi khusus untuk suatu aplikasi pada versi tertentu. 

## Aplikasi Django tanpa Virtual Environment
Sebuah aplikasi tentunya bisa dibuat tanpa Virtual Environment. Namun, seperti yang dijelaskan sebelumnya, suatu aplikasi dapat memiliki _dependencies_ yang berbeda tergantung dengan versi aplikasi yang kita buat. Jika kita menjalankan aplikasi tanpa Virtual Environment, aplikasi akan jalan dengan modul yang global saja dan saat kita melakukan upgrade, akan ada kemungkinan tidak bisa berjalan karena fungsi yang sudah berubah dan tidak lagi sesuai dengan kebutuhan aplikasi. Jika kita ingin membuat suatu aplikasi yang tidak akan di_upgrade_ atau digunakan hanya sementara, kita bisa membuatnya tanpa Virtual Environment.

## Cara implementasi
1. Membuat fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
Membuat fungsi katalog_view dengan parameter _request_ dari user. Fungsi tersebut akan memanggil query ke dalam database dan menyimpan hasil dalam variabel catalogitem kemudian katalog.html akan dirender agar dapat muncul dalam HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.

Routing dilakukan dengan menambahkan path('katalog/', include('katalog.urls')) pada urls.py di project_django. Routing dilakukan ke urls.py pada katalog. Kemudian urls.py ini akan menjalankan fungsi view show_katalog yang berada di views.py.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django
Pemetaan dari proses render dengan fungsi pada views.py pada katalog.html. Akan dilakukan pemetaan dari data yang ada.

4. Melakukan deployment
Untuk melakukan deployment, hubungkan repository pada github dengan heroku. Tambahkan variable APP_NAME dan API_KEY dari aplikasi yang kita buat di Heroku ke dalam Github repository secrets.