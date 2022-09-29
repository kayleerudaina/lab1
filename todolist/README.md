# Tugas 4 PBP
Link aplikasi : [todolist](https://newappmvt.herokuapp.com/todolist/) 

## Kegunaan {% csrf_token %} pada elemen form
Serangan _Cross-Site Request Forgery_ (CSRF) adalah serangan yang umum terjadi yang membuat pengguna mengirim sebuah _request_ ke website walaupun _request_ tersebut tidak dimaksud untuk dilakukan oleh user. {% csrf_token %} merupakan suatu token dari Django yang digunakan untuk melindungi web dari serangan CSRF. Jika token ini tidak digunakan, serangan lebih rentan terjadi.

## Cara membuat form secara manual
 Kita dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti dengan membuat `<form>` yang bisa diisi oleh user dan bisa diambil datanya secara manual menggunakan `<label>` dan `<input>`. Render secara manual bisa dilakukan dengan `{{ form.name_of_field }}`

## Proses alur data
Proses submisi dimulai saat pengguna menekan tombol 'Submit' pada form create task. Kemudian data akan dicek dahulu validitasnya, jika valid, data baru disimpan dalam database. Jika sudah disimpan dalam database, untuk melihatnya lagi kita mengakses dengan `Models.objects.filter(user=request.user)`. Data dapat ditampilkan dengan memasukkan context pada fungsi views.


## Cara implementasi
1. Membuat aplikasi baru, yaitu todolist dan menambahkan pada INSTALLED_APPS dalam settings.py di project_django
2. Menambahkan path baru untuk aplikasi mywatchlist dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada urls.py di project_django
3. Membuat model baru TodoItem sebagai model Task beserta atributnya di models.py
4. Dalam views.py membuat fungsi untuk implementasi registrasi akun, login, logout dan membuat task baru. Semua fungsi, kecuali fungsi untuk registrasi akun, dibuat untuk kembali ke halaman utama todolist. 
5. Agar  halaman utama dan halaman membuat task baru hanya bisa diakses oleh user yang sudah login, ditambahkan `@login_required(login_url='/todolist/login/')` diatas fungsi masing-masing.
6. Membuat berkas `register.html`, `login.html`, `create.html`, dan `todolist.html` dalam templates sebagai tampilan dari masing-masing halaman.
7. Menambahkan routing untuk fungsi login, logout, register dan create-task pada urls.py.
8. Melakukan deployment dengan menghubungkan repository pada github dengan Heroku. 