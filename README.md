# Laporan Proyek Machine Learning
### Nama : Ardi Nursahwal
### Nim : 211351022
### Kelas : Malam B

## Domain Proyek

Ikan merupakan sumber protein yang berguna untuk mereka yang sedang melakukan diet daging merah dan menggunakan ikan sebagai pengganti sumber proteinnya. Penjualan ikan pun terus meningkat dari waktu ke waktu dikarenakan permintaan ikan yang meningkat.

## Business Understanding

Proyek ini dibuat untuk mempermudah siapapun yang ingin mengetahui estimasi berat ikan Perch, Bream, Roach, Pike,Smelt,Parkki dan Whitefish tanpa perlu menimbangnya secara langsung. Model ini dibuat untuk mendapatkan estimasi berat ikan dalam satuan gram dengan inputan :

berat ikan dalam gram
panjang vertikal dalam cm
panjang diagonal dalam cm
panjang silang dalam cm
tinggi dalam cm
lebar diagonal dalam cm
menggunakan algoritma regresi linear.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- sulitnya mengetahui berat ikan jika tidak memiliki timbangan
- sulitnya mengetahui berat ikan tanpa harus menimbangnya secara langsung

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- dapat mempermudah masyarakat dalam mengetahui berat ikan jika mereka tidak memiliki timbangan/tidak memegang ikannya secara langsung 

    ### Solution statements
    - Membuat model estimasi berat ikan menggunakan metode estimasi dengan algoritma regresi linear
    - Deploy model yang sudah di buat agar dapat diakses oleh masyarakat umum
    - 
## Data Understanding
Dataset pasar ikan adalah kumpulan data yang terkait dengan berbagai spesies ikan dan karakteristiknya. Dataset ini disusun sedemikian rupa sehingga setiap baris berhubungan dengan satu ikan dengan spesiesnya dan berbagai ukuran fisik (panjang, tinggi, dan lebar)

dataset: [Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Dataset adalah sebagai berikut:
- Spesies : Nama spesies ikan ('Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt')
- Weight: Berat ikan dalam gram
- Length1: Panjang vertikal ikan dalam CM
- Length2: Panjang diagonal ikan dalam CM
- Length3: Panjang silang ikan dalam CM
- Height: Tinggi ikan dalam CM
- Width: Lebar diagonal ikan dalam CM

## Data Preparation
Pengecekan nilai yang kosong dalam dataset:
```
sns.heatmap(df.isnull())
```

![image](https://github.com/ardinursahwal/estimasi-berat-ikan/assets/148542995/4839e542-fd6b-4eb4-9b8b-0aa8e0178a92)

cek korelasi antar antribut:
```
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True)
```
![image](https://github.com/ardinursahwal/estimasi-berat-ikan/assets/148542995/4a92cd55-61c0-443d-98db-b96be4cb0e38)

Hasil yang cukup bagus, lanjut ketahapan selanjutnya.

Pada tahapan data preparation yang dilakukan tidaklah banyak dikarenakan dataset yang dipakai sudah nyaris sesuai dengan algoritma yang digunakan. dikarenakan ada 1 kolom yang memiliki tipe data object maka perlu dilakukan konversi tipe data menjadi integer dengan cara:
```bash
label_encoder = LabelEncoder()

# Terapkan LabelEncoder pada kolom 'smoker' dan simpan dalam kolom baru 'smoker2'
df['Species2'] = label_encoder.fit_transform(df['Species'])
```
Visualisasi jumlah ikan berdasarkan spesies:
```
Specieses = df.groupby('Species').count()[['Width']].reset_index()
Specieses = Specieses.rename(columns={'Width':'Number Of Fishes'})
```
```
fig = plt.figure(figsize=(15,5))
sns.barplot(x=Specieses['Species'], y=Specieses['Number Of Fishes'], color='royalblue')
plt.xticks(rotation=60)
plt.show()
```
![image](https://github.com/ardinursahwal/estimasi-berat-ikan/assets/148542995/4ad144f5-b691-4397-ac8f-9dbcdbd65e5b)

## Modeling
1. Seleksi fitur:
```bash
features = df.drop(['Weight','Species'], axis=1)
x = features
y = df['Weight']
x.shape, y.shape
```
3. Memisahkan data training dan testing
```bash
from sklearn.model_selection import train_test_split
x_train, X_test, y_train, y_test = train_test_split(x,y,random_state=70)
y_test.shape
```
5. Pembuatan model Regresi Linear
```bash
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)
pred = lr.predict(X_test)
```


## Evaluation
Metrik evaluasi yang digunakan adalah akurasi:
```bashscore = lr.score(X_test, y_test)
print('akurasi model regresi linier = ', score*100,"%")
```
akurasi yang didapatkan adalah 85.17% yang mana menunjukan jika model yang dibuat masih tergolong bagus dan dapat dipakai.

## Deployment
[Estimasi Berat Ikan](https://tugas-uts-ardi.streamlit.app/)
