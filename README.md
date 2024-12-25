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
  ![Split Dataset_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/split.png)
  ![Split Dataset_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/split.png)
- 🏗️ **Layering pada VGG16:**
  ![Layering_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/layering.png)
  ![Layering_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/layer_cnn.png)
- 📈 **Training History:**
  ![Training History_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/training.png)
  ![Training History_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/train_cnn.png)
- 🔍 **Confusion Matrix:**
  ![Confusion Matrix_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/cm.png)
  ![Confusion Matrix_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/cm_cnn.png)
- 🧪 **Evaluasi Model:**
  ![Evaluasi Model_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/eval.png)
  ![Evaluasi Model_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/eval_cnn.png)
- 📊 **Visualisasi:**
  ![Visualisasi_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/visualisas.png)
  ![Visualisasi_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/visual_cnn.png)
- 📜 **Classification Report:**
  ![Classification Report_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/cr.png)
  ![Classification Report_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/cr_cnn.png)
- 💾 **Saving Model:**
  ![Saving Model_VGG16](C:/Users/MSI-PC/Documents/uap/src/uap/image/saving.png)
  ![Saving Model_CNN](C:/Users/MSI-PC/Documents/uap/src/uap/image/save_cnn.png)

---

### 🏆 Hasil Akhir

1. **Akurasi Model:**
   - CNN : Mencapai akurasi test sebesar **89%**.
   - VGG16 : Mencapai akurasi test sebesar **98%**.
2. **Aplikasi Web:**
   - Aplikasi berhasil memproses dan menampilkan hasil prediksi secara real-time.

# **💡 Model : https://drive.google.com/drive/folders/1sZSb7yVN1Pzxxr_aiDQKjRX4FRtd08qj?usp=sharing**
