# Deployment Model Analisis Sentimen menggunakan LSTM (Long Short Term Memory) 

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Analisis Sentimen menggunakan LSTM (Long Short Term Memory) . Adapun model yang digunakan merupakan model untuk memprediksi sentimen apakah termasuk sentimen positif, netral atau negatif.

#

## Sekilas mengenai input model

Agar dapat sentimen, data input model harus mengikuti format sebagai berikut:

-   terdiri dari teks dengan maksimal 5000 kata.

#

## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website.
-   app.py --> Berisi konfigurasi route dan proses prediksi model untuk API.
-   best_model1.hdf5 --> Model Analisis Sentimen dengan LSTM yang sudah di-training.
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Analisis Sentimen dengan LSTM.

#

## Cara menjalankan API pada komputer Anda

1. Pastikan Anda sudah menginstall Anaconda.
1. Buka terminal/command prompt/power shell.
1. Buat virtual environment dengan\
   `conda create -n <nama-environment> python=3.9`
1. Aktifkan virtual environment dengan\
   `conda activate <nama-environment>`
1. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
3. Jalankan API menggunakan perintah\
   `python app.py`

## Akses melalui Website

1. Anda akan diberikan URL untuk membuka website berupa `127.0.0.1:5002/`.
2. Buka URL dengan browser, coba masukkan teks yang ingin di prediksi.
3. Anda akan diberikan prediksi dari teks serta tabel matriksnya
