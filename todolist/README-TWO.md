# Tugas 6 PBP
Link aplikasi : [todolist](https://newappmvt.herokuapp.com/todolist/) 

## Perbedaan _Asynchronous Programming_ dengan _Synhcronous Programming_
Asynchronous programming berarti bahwa proses eksekusi bisa dilakukan secara bersamaan tanpa melihat urutannya. Programming secara async dilakukan saat melakukan operasi-operasi yang tidak menunggu proses lainnya. Sedangkan, synchronous programming berarti proses ekesekusi berjalan secara _sequential_ atau sesuai tahapan eksekusinya.

## Paradigma _Event-Driven Programming_
_Event-Driven Programming_ adalah proses pemrograman dimana suatu program akan berjalan sesuai dengan event interaksi user yang terjadi atau pesan dalam program. Event dapat berupa input dari user atau misal User melakukan penambahan _todo_ baru dalam program todolist.

## _Asynchronous Programming_ pada AJAX
Dalam penerapan AJAX, AJAX akan menampung terlebih dahulu data yang diberikan oleh user kemudian dikirim ke server untuk melakukan update secara async. Kemudian, saat kondisi AJAX berada dalam GET atau POST, data akan dikirim ke server dan ter_update_ tanpa reload. Seluruh proses ini dilakukan dengan paradgima _event-driven programming_ yang tertrigger oleh data yang dimasukkan oleh user.

## Cara implementasi
1. Membuat fungsi show_ajax pada views.py yang akan mengembalikan data todo dalam bentuk JSON.
2. Membuat route ke todolist/json untuk memanggil fungsi show_ajax
3. Menampilkan cards todolist yang telah dibuat dengan GET dari JSON.
4. Membuat modal untuk menambahkan todo baru, setelah di_submit_ akan dimasukkan ke dalam fungsi kemudian data dari modal akan dirimkan dengan AJAX POST.
5. Data yang telah dikirim akan dibuat menjadi sebuah card baru.
