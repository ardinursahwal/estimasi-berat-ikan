# Laporan Proyek Machine Learning
### Nama : Ardi Nursahwal
### Nim : 211351022
### Kelas : Malam B

## Domain Proyek

Ikan sangat penting di Indonesia karena merupakan sumber mata pencaharian bagi jutaan nelayan, mendukung ekonomi lokal, dan berperan dalam ekosistem laut yang penting bagi keseimbangan lingkungan. Indonesia adalah salah satu negara dengan keragaman hayati laut yang luar biasa, dan konservasi serta pengelolaan sumber daya ikan menjadi kunci dalam menjaga kelangsungan hidup ikan dan mendukung kehidupan berkelanjutan di kepulauan Indonesia. 

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Dataset pasar ikan adalah kumpulan data yang terkait dengan berbagai spesies ikan dan karakteristiknya. Dataset ini disusun sedemikian rupa sehingga setiap baris berhubungan dengan satu ikan dengan spesiesnya dan berbagai ukuran fisik (panjang, tinggi, dan lebar)

dataset: [Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Dataset adalah sebagai berikut:
- Weight: Kolom ini menunjukkan berat ikan. Ini adalah variabel numerik yang biasanya diukur dalam gram. Berat adalah variabel dependen yang ingin kita prediksi menggunakan regresi polinomial.
- Length1: Kolom ini mewakili pengukuran pertama dari panjang ikan. Ini adalah variabel numerik, biasanya diukur dalam sentimeter.
- Length2: Kolom ini mewakili pengukuran kedua dari panjang ikan. Ini adalah variabel numerik lain, biasanya diukur dalam sentimeter.
- Length3: Kolom ini mewakili pengukuran ketiga dari panjang ikan. Mirip dengan dua kolom sebelumnya, ini adalah variabel numerik, biasanya diukur dalam sentimeter.
- Height: Kolom ini mewakili tinggi ikan. Ini adalah variabel numerik, biasanya diukur dalam sentimeter.
- Width: Kolom ini mewakili lebar ikan. Seperti variabel numerik lainnya, ini juga biasanya diukur dalam sentimeter.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment
[Estimasi Berat Ikan](https://tugas-uts-ardi.streamlit.app/)
**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

