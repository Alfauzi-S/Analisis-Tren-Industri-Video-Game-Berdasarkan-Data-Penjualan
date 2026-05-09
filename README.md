# Analisis Pengaruh Skor Kritikus dan Skor Pengguna terhadap Penjualan Global Video Game

Proyek ini merupakan implementasi dari penelitian yang berjudul **"Analisis Pengaruh Skor Kritikus dan Skor Pengguna terhadap Penjualan Global Video Game Menggunakan Metode Regresi Linear Berganda"**. Penelitian ini menggunakan data sekunder dari Kaggle untuk menganalisis hubungan antara *Critic Score* dan *User Score* terhadap *Global Sales* video game.

## 📁 Dataset

- **Sumber**: [Video Game Sales with Ratings](https://www.kaggle.com/datasets/gregorut/videogamesales) (Kaggle)
- **Deskripsi**: Dataset ini berisi 16.598 baris dan 16 kolom, mencakup informasi tentang penjualan global, skor kritikus, skor pengguna, platform, genre, dan lain-lain untuk ribuan judul game dari tahun 1980 hingga 2016.
- **Nama file**: `Video_Games_Sales_as_at_22_Dec_2016.csv`
- **Preprocessing**:
  - Konversi kolom `User_Score` dari string ke numerik
  - Penghapusan baris dengan missing values pada `Global_Sales`, `Critic_Score`, dan `User_Score`
  - **Jumlah sampel akhir**: 7.017 data observasi valid

## 📊 Metodologi

- **Analisis Korelasi**: Pearson correlation matrix
- **Model Regresi**: Multiple Linear Regression dengan metode **Ordinary Least Squares (OLS)**
- **Evaluasi**: R-squared, uji F, uji t

## 📈 Hasil Utama

### 1. Matriks Korelasi Pearson

![Heatmap Korelasi](./Screenshot%202026-05-09%20123457.png)

### 2. Model Regresi

Persamaan regresi:
```
Global_Sales = -1.2662 + 0.0391*(Critic_Score) - 0.0997*(User_Score)
```

![OLS Output](./Screenshot%202026-05-09%20123507.png)

**Interpretasi:**
- **R-squared**: 0.060
- **F-statistic**: 223.0 (p < 0.001)
- **Kesimpulan**: Model signifikan secara statistik; *Critic Score* berpengaruh positif terhadap penjualan global, sementara *User Score* menunjukkan pengaruh negatif yang kontraintuitif (mungkin karena bias waktu).

### 3. Visualisasi

**Scatter plot dan garis regresi (Critic Score vs Global Sales):**  
![Scatter Plot](./Screenshot%202026-05-09%20123451.png)

**Diagram alir tahapan penelitian:**  
![Diagram Alir](./Screenshot%202026-05-09%20173150.png)

## 🔧 Cara Menjalankan

1. Pastikan Anda memiliki Python 3.7+ dan pustaka yang diperlukan:
   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels
   ```

2. Clone repository ini dan pastikan file `Video_Games_Sales_as_at_22_Dec_2016.csv` berada di direktori yang sama.

3. Jalankan skrip utama (misalnya `main.py`):
   ```bash
   python main.py
   ```

   Skrip akan menampilkan:
   - Matriks korelasi
   - Ringkasan model regresi
   - Scatter plot + garis regresi
   - Heatmap korelasi

## 📂 Struktur Repository

```
├── README.md
├── main.py                          # kode sumber utama (analisis regresi)
├── Video_Games_Sales_as_at_22_Dec_2016.csv
├── Screenshot 2026-05-09 123451.png   # scatter plot
├── Screenshot 2026-05-09 123457.png   # heatmap korelasi
├── Screenshot 2026-05-09 123507.png   # output OLS
├── Screenshot 2026-05-09 173150.png   # diagram alir
├── Screenshot 2026-05-09 173155.png   # (gambar tambahan)
├── Screenshot 2026-05-09 173159.png   # (gambar tambahan)
└── Jurnal Analisis Pengaruh Skor Kritikus...pdf   # naskah lengkap
```

## 📖 Referensi

Dataset: [Kaggle - Video Game Sales with Ratings](https://www.kaggle.com/datasets/gregorut/videogamesales)  
Metode: Montgomery et al. (2012), Draper & Smith (1998), Hair et al. (2014), dll.

## 📝 Lisensi

Proyek ini menggunakan dataset dengan lisensi publik. Kode sumber dapat digunakan untuk keperluan akademik dan non-komersial.

---

**Kontributor**: Muhammad Alfauzi Syahputra, K. Destiana, Zihni Larasati  
**Program Studi Informatika, Universitas Mulawarman**
