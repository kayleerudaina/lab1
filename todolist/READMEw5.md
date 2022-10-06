# Tugas 5 PBP
Link aplikasi : [todolist](https://newappmvt.herokuapp.com/todolist/) 


## Perbedaan Inline, Internal dan External CSS
- Inline digunakan untuk tag HTML tertentu. Atribut `<style>` digunakan untuk memberikan style ke tag HTML tertentu. Cara ini sedikit rumit karena bisa jadi setiap tag harus diberikan style masing-masing. Namun cara ini berguna untuk perbaikan cepat.
- Internal CSS merupakan cara dengan meletakkan kode CSS dalam bagian `<head>` pada halaman sehingga perubahan hanya terjadi pada halaman tersebut. Style CSS dengan metode ini akan di-download setiap kali halaman dipanggil sehingga waktu akses website meningkat.
- External CSS merupakan cara menambahkan CSS ke website dari file `.css` external. Karena file css external, ukuran file HTML lebih kecil dan kecepatan loading lebih cepat. File CSS juga bisa digunakan untuk beberapa halaman sekaligus. Namun, karena file external, halaman tidak bisa tampil sempurna sehingga file CSS selesai dipanggil

## Tag HTML5
Tag elemen merupakan penanda awalan dan akhir sebuah elemen dalam HTML.
1. `<html>` untuk memulai dokumen HTML
2. `<head>`, `<body>` untuk bagian head dan body
3. `<h1>`- `<h6>` untuk membuat heading

## Tipe CSS Selector
"." untuk selector class dari sebuah komponen, "#" untuk select id yang ditambahkan dalam sebuah komponen, child selector > untuk memilih semua elemen yang di dalam sebuah komponen. Hal paling basic adalah element selector untuk memilih elemen yang digunakan, contohnya h1, body, atau lain-lain.

## Cara Implementasi