# 🌾 Web Deploy Streamlit : Analisis Performa CNN dengan VGG16 untuk Klasifikasi Jenis Beras

---

## 🎀✨ Nama: Kens Urganis Awangsari Puttrisia Soenarto 
## 🐾💖 NIM: 202110370311273

---

Proyek ini bertujuan untuk menciptakan  **model klasifikasi jenis beras** menggunakan **Convolutional Neural Network (CNN)** berbasis arsitektur **VGG16** dengan platform VSCode. Selain itu, proyek ini dilengkapi dengan **aplikasi web interaktif** berbasis Streamlit untuk memvisualisasikan hasil klasifikasi secara real-time.

---

### 🚀 Fitur Utama

1. **Klasifikasi Beras:**
   - Model mendukung klasifikasi 5 jenis beras: `Basmati`, `Arborio`, `Ipsala`, `Karacadag`, dan `Jasmine`.
     
2. **Web Aplikasi:**
   - Upload gambar atau dataset.
   - Prediksi langsung guna untuk mendeteksi skor dataset yang telah diupload.
   - Tampilan prediksi berupa tabel dan dapat diunduh dengan format .csv atau .xlsx.
   - Simpan image atau dataset yang telah di upload ke dalam folder saved_images pada folder yang tersedia.
     
3. **Analisis Performa:**
   - Training History,
   - Confusion Matrix, dan
   - Laporan Klasifikasi.

---

### 📂 Struktur Proyek

#### 1. Persiapan

**Langkah-langkah awal:**
- Buat folder proyek baru.
- Atur lingkungan virtual dan instal pustaka yang diperlukan:

```bash
python -m venv myenv
myenv/Scripts/activate
pip install pdm
pdm init
pip install streamlit tensorflow joblib scikit-learn
```

**Buat folder tambahan:**
- `model`: Untuk menyimpan file model hasil training.

#### 2. Dataset

- Dataset yang digunakan: [Rice Image Dataset](https://www.kaggle.com/datasets/ayanwap7/rice-image-dataset-train-test-split).
- Struktur dataset: Folder `train` dan `test`.
- Classes : `Basmati`, `Arborio`, `Ipsala`, `Karacadag`, dan `Jasmine`.

---

### 🧠 Pembuatan Model: `vgg_citra.py`

**Langkah-langkah utama:**

1. **Preprocessing Data:**
   - Augmentasi gambar: Rescaling, rotation, dan horizontal flip.

2. **Arsitektur Model:**
   - Menggunakan **VGG16** pre-trained model.
   - Layer tambahan untuk klasifikasi 5 kelas beras.

3. **Evaluasi Model:**
   - **Training History**: Akurasi dan loss selama training.
   - **Confusion Matrix** dan **Classification Report**.

4. **Menyimpan Model:**
   - Model disimpan dalam format `.h5` di folder `model`.

---

### 🌐 Pengembangan Aplikasi Web

#### File Utama:

1. **`dashboard.py`:**
   - Menyediakan tampilan dashboard interaktif.
   - Menampilkan hasil prediksi, deskripsi, dan navigasi gambar.

2. **`app.py`:**
   - Menghubungkan semua modul Streamlit.

**Menjalankan aplikasi:**
```bash
cd src/uap_ml
pdm run streamlit run app.py
```

---

### 📊 Visualisasi & Hasil Akhir

**Fitur visualisasi:**
1. **Split Dataset:**
   - Distribusi data `train` dan `test`.
2. **Arsitektur Model:**
   - Visualisasi struktur layer VGG16.
3. **Training History:**
   - Grafik akurasi dan loss.
4. **Evaluasi Model:**
   - Confusion Matrix dan laporan klasifikasi.

**Tampilan:**
- 📸 **Split Dataset:**
  
  ![split](https://github.com/user-attachments/assets/024374bc-1dfb-4ab8-b40a-dca41c561b58)
  
- 🏗️ **Layering pada VGG16:**
  
  ![layer_cnn](https://github.com/user-attachments/assets/93ee9e33-0b08-4b27-afa2-6a5b8707b52a)

  ![layering](https://github.com/user-attachments/assets/b3f2e301-f820-4381-83f6-943756eded3c)

- 📈 **Training History:**
  
  ![training](https://github.com/user-attachments/assets/551954d4-b190-47a8-b987-e29e47e9fe35)

  ![train_cnn](https://github.com/user-attachments/assets/2696396c-dabb-46f4-8374-07daa640f285)

- 🧪 **Evaluasi Model:**
  
  ![eval_cnn](https://github.com/user-attachments/assets/ac897c5f-0172-48b3-9d68-4b6b60cf1a6d)

  ![eval](https://github.com/user-attachments/assets/53df076f-fc68-4d14-9574-d9daf2cd7a5d)

- 📊 **Visualisasi:**
  
  ![visualisas](https://github.com/user-attachments/assets/dd72cab1-b65f-4906-8206-b4bd38130010)

  ![visual_cnn](https://github.com/user-attachments/assets/112b1634-80e6-4d52-b646-ff6fe190b364)

- 📜 **Classification Report:**
  
  ![cr](https://github.com/user-attachments/assets/2e412b52-7b1b-4e4b-a29f-5ee6bdd8d579)

  ![cr_cnn](https://github.com/user-attachments/assets/7b0e2ac7-8906-4e60-88a5-ad430b6dc303)

- 🔍 **Confusion Matrix:**
  
  ![cm](https://github.com/user-attachments/assets/5c046e2a-1ae8-4303-96dc-7ba4e62f3490)

  ![cm_cnn](https://github.com/user-attachments/assets/3f542c5d-12cb-49a8-b25c-16ea1426b9cc)

- 💾 **Saving Model:**
  
  ![saving](https://github.com/user-attachments/assets/27c2988a-8d21-43c8-9bc3-0ac689e66744)

  ![save_cnn](https://github.com/user-attachments/assets/c4470a16-b5a5-4d03-879d-c10c6fd3eab1)


---

### 🏆 Hasil Akhir

1. **Akurasi Model:**
   - CNN : Mencapai akurasi test sebesar **89%**.
   - VGG16 : Mencapai akurasi test sebesar **98%**.
2. **Aplikasi Web:**
   - Aplikasi berhasil memproses dan menampilkan hasil prediksi secara real-time.

# **💡 Model : https://drive.google.com/drive/folders/1sZSb7yVN1Pzxxr_aiDQKjRX4FRtd08qj?usp=sharing**
