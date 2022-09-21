# Tugas 3 PBP
Link aplikasi : [mywatchlist](https://newappmvt.herokuapp.com/mywatchlist/) 

## Perbedaan JSON, XML dan HTML

1. JSON diperlukan untuk menyimpan dan transfer data hingga dapat dibaca oleh pengguna, penulisannya menggunakan objek JavaScript. Perbedaannya dengan XML, Struktur kode dari JSON lebih sederhana dan lebih mudah untuk dipahami, proses penerapannya juga lebih cepat. Format JSON juga bisa digunakan ke berbagai *programming language*.
2. XML, sama seperti JSON, diperlukan untuk menyimpan data dan pertukaran data. XML seringkali dianggap mirip dengan HTML karena keduanya merupakan bahasa markup tetapi keduanya memiliki fungsi yang berbeda.
3. HTML adalah bahasa markup diperlukan untuk menampilkan data bertujuan untuk penyajian data dan tidak bisa digunakan untuk pertukaran data. Data pada HTML dapat diakses dan ditampilkan melalui web.

## Mengapa memerlukan data delivery dalam pengimplementasian sebuah platform

Data delivery diperlukan untuk melakukan pertukaran data antarserver. Data terdapat dalam banyak bentuk, antara lain XML, JSON dan HTML. Data delivery akan mempercepat proses pengiriman data dalam berbentuk yang berbeda-beda dalam suatu platform.

## Cara implementasi

1. Membuat aplikasi baru, yaitu mywatchlist dan menambahkan pada settings.py dalam project_django
2. Menambahkan path baru untuk aplikasi mywatchlist dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada urls.py di project_django
3. Membuat model baru MyWatchlist beserta atributnya
4. Memetakan data XML dan JSON dengan menambahkan `path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'),` pada urls.py dalam mywatchlist untuk bisa menunjukkan data dalam bentuk XML dan JSON.
4. Melakukan deployment dengan menghubungkan repository pada github dengan Heroku. 