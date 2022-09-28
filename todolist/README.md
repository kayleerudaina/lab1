# Tugas 4 PBP
Link aplikasi : [todolist](https://newappmvt.herokuapp.com/todolist/) 

## Kegunaan {% csrf_token %} pada elemen <form>

Serangan _Cross-Site Request Forgery_ (CSRF) merupakan serangan yang umum terjadi yang membuat pengguna mengirim sebuah _request_ ke website walaupun _request_ tersebut tidak dimaksud untuk dilakukan oleh user. {% csrf_token %} digunakan untuk melindungi web dari serangan CSRF. 

## Mengapa memerlukan data delivery dalam pengimplementasian sebuah platform

Data delivery diperlukan untuk melakukan pertukaran data antarserver. Data terdapat dalam banyak bentuk, antara lain XML, JSON dan HTML. Data delivery akan mempercepat proses pengiriman data dalam berbentuk yang berbeda-beda dalam suatu platform.

## Cara implementasi

1. Membuat aplikasi baru, yaitu mywatchlist dan menambahkan pada settings.py dalam project_django
2. Menambahkan path baru untuk aplikasi mywatchlist dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada urls.py di project_django
3. Membuat model baru MyWatchlist beserta atributnya
4. Memetakan data XML dan JSON dengan menambahkan `path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'),` pada urls.py dalam mywatchlist untuk bisa menunjukkan data dalam bentuk XML dan JSON.
4. Melakukan deployment dengan menghubungkan repository pada github dengan Heroku. 