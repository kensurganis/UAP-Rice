import streamlit as st
import tensorflow as tf
import os
import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# --- Custom Styling ---
def apply_custom_style():
    st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #F0FFF0; /* Light green */
        }

        /* Sidebar Styling */
        .stSidebar {
            background-color: #F7F7F7;
        }

        /* Title Styling */
        h1 {
            color: #2E8B57; /* SeaGreen */
        }

        /* Button Styling */
        .stButton > button {
            background-color: #4CAF50; /* Green */
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 15px;
            font-size: 16px;
            margin: 5px;
        }
        .stButton > button:hover {
            background-color: #45a049; /* Darker green */
        }

        /* Expander Border Styling */
        .st-expander {
            border-radius: 8px;
            border: 1px solid #4CAF50;
        }

        /* Table Styling */
        .dataframe {
            border: 1px solid #4CAF50;
            border-radius: 8px;
            padding: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

apply_custom_style()

# --- MENU ---
with st.sidebar.expander("Menu Navigasi", expanded=True):
    menu = st.selectbox("Pilih Menu", 
                        ("Dashboard", "Upload Dataset/Image", "Prediksi Data/Image", "Tampilkan Hasil Prediksi", "Simpan Data/Image"))

# Global variable for uploaded images and history
if 'uploaded_image_paths' not in st.session_state:
    st.session_state['uploaded_image_paths'] = []

if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- DASHBOARD ---
if menu == "Dashboard":
    st.header("Selamat datang di Dashboard Klasifikasi Citra.")

    # Dummy data untuk gambar hasil klasifikasi
    cnn_images = [
        {"path": "./image/split.png", "title": "CNN - Gambar 1", "desc": "Split Dataset Rice Image"},
        {"path": "./image/layer_cnn.png", "title": "CNN - Gambar 2", "desc": "Layering pada Klasifikasi VGG16 Dataset Rice Image"},
        {"path": "./image/train_cnn.png", "title": "CNN - Gambar 3", "desc": "Training Dataset Rice Image dengan 10 Epoch dengan Hasil Akhir 0.95"},
        {"path": "./image/visual_cnn.png", "title": "CNN - Gambar 4", "desc": "Hasil Visualisasi dari Proses Training Dataset yang Terdapat Indikasi Overfitting pada Loss"},
        {"path": "./image/eval_cnn.png", "title": "CNN - Gambar 5", "desc": "Hasil Evaluasi Test Accuracy dan Loss Dataset Rice Image"},
        {"path": "./image/cr_cnn.png", "title": "CNN - Gambar 6", "desc": "Classification Report Dataset Rice Image"},
        {"path": "./image/cm_cnn.png", "title": "CNN - Gambar 7", "desc": "Confusion Matrix Dataset Rice Image"},
        {"path": "./image/save_cnn.png", "title": "CNN - Gambar 8", "desc": "Save Model CNN ke .h5"},
    ]

    vgg16_images = [
        {"path": "./image/split.png", "title": "VGG16 - Gambar 1", "desc": "Split Dataset Rice Image"},
        {"path": "./image/layering.png", "title": "VGG16 - Gambar 2", "desc": "Layering pada Klasifikasi VGG16 Dataset Rice Image"},
        {"path": "./image/training.png", "title": "VGG16 - Gambar 3", "desc": "Training Dataset Rice Image menggunakan VGG16 dengan 10 Epoch dengan Hasil Akhir 0.98"},
        {"path": "./image/visualisas.png", "title": "VGG16 - Gambar 4", "desc": "Hasil Visualisasi dari Proses Training Dataset yang Terdapat Indikasi Overfitting pada Loss"},
        {"path": "./image/eval.png", "title": "VGG16 - Gambar 5", "desc": "Hasil Evaluasi Test Accuracy dan Loss Dataset Rice Image"},
        {"path": "./image/cr.png", "title": "VGG16 - Gambar 6", "desc": "Classification Report Dataset Rice Image"},
        {"path": "./image/cm.png", "title": "VGG16 - Gambar 7", "desc": "Confusion Matrix Dataset Rice Image"},
        {"path": "./image/saving.png", "title": "VGG16 - Gambar 8", "desc": "Save Model VGG16 ke .h5"},
    ]

    # cnn
    st.header(">> CNN <<")
    st.write("CNN digunakan untuk klasifikasi citra dengan arsitektur sederhana namun kuat.")
    for img in cnn_images:
        with st.expander(f"**{img['title']}**"):
            if os.path.exists(img["path"]):
                st.image(img["path"], caption=img["title"], use_container_width=True)
                st.write(f"**{img['title']}**")
                st.write(img["desc"])
            else:
                st.warning(f"Gambar {img['title']} tidak ditemukan.")

    # vgg16
    st.header(">> VGG16 <<")
    st.write("VGG16 adalah model klasifikasi dengan akurasi tinggi untuk dataset citra kompleks.")
    for img in vgg16_images:
        with st.expander(f"**{img['title']}**"):
            if os.path.exists(img["path"]):
                st.image(img["path"], caption=img["title"], use_container_width=True)
                st.write(f"**{img['title']}**")
                st.write(img["desc"])
            else:
                st.warning(f"Gambar {img['title']} tidak ditemukan.")

# --- UPLOAD DATASET/IMAGE ---
if menu == "Upload Dataset/Image":
    st.header("Unggah Dataset atau Citra")
    st.info("Silakan unggah file gambar dengan format JPG, PNG, atau JPEG.")
    
    # Upload multiple images
    uploaded_files = st.file_uploader("Pilih citra atau dataset", 
                                      type=["png", "jpg", "jpeg"], 
                                      accept_multiple_files=True)
    
    if uploaded_files:
        st.session_state['uploaded_image_paths'] = []
        saved_images_path = "saved_images"
        if not os.path.exists(saved_images_path):
            os.makedirs(saved_images_path)
        
        for uploaded_file in uploaded_files:
            if uploaded_file.name.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(saved_images_path, uploaded_file.name)
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                st.image(image_path, caption=f"Gambar: {uploaded_file.name}")
                st.success(f"Gambar '{uploaded_file.name}' berhasil diunggah dan disimpan.")
                st.session_state['uploaded_image_paths'].append(image_path)

            if st.button("Reset Gambar yang Diunggah", key="reset_uploads"):
                st.session_state['uploaded_image_paths'] = []
                st.success("Daftar gambar telah di-reset.")

# --- PREDIKSI DATA/IMAGE ---
elif menu == "Prediksi Data/Image":
    st.header("Prediksi Citra")

    if st.session_state['uploaded_image_paths']:
        class_names = ["Basmati", "Arborio", "Ipsala", "Karacadag", "Jasmine"]

        try:
            # Load model
            model_path = "C:/Users/MSI-PC/Documents/uap/src/uap/model/citra_cnn.h5"
            if not os.path.exists(model_path):
                st.error("Model tidak ditemukan.")
                st.stop()

            model = tf.keras.models.load_model(model_path)

            predictions = []
            for image_path in st.session_state['uploaded_image_paths']:
                img = tf.keras.utils.load_img(image_path, target_size=(128, 128))
                img_array = tf.keras.utils.img_to_array(img)
                img_array = tf.expand_dims(img_array, 0)

                # Prediction
                output = model.predict(img_array)
                score = tf.nn.softmax(output[0])

                all_scores = {class_name: round(float(prob) * 100, 2) for class_name, prob in zip(class_names, score)}
                pred_class = max(all_scores, key=all_scores.get)

                st.image(image_path, caption=f"Gambar: {os.path.basename(image_path)}")

                # Display the table with prediction results
                result_df = pd.DataFrame({
                    "Kelas": list(all_scores.keys()),
                    "Skor Keyakinan (%)": list(all_scores.values())
                })
                st.table(result_df)

                # Display the bar plot for the prediction scores
                fig, ax = plt.subplots()
                ax.barh(list(all_scores.keys()), list(all_scores.values()), color='skyblue')
                ax.set_xlabel("Skor (%)")
                ax.set_title(f"Hasil Prediksi - {os.path.basename(image_path)}")
                st.pyplot(fig)

                # Save prediction results
                predictions.append({
                    "Nama Gambar": os.path.basename(image_path),
                    "Prediksi Kelas": pred_class,
                    "Skor": all_scores
                })

            # Save predictions to history
            st.session_state['history'].extend(predictions)
            st.success("Hasil prediksi berhasil disimpan.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Silakan unggah gambar terlebih dahulu melalui menu 'Upload Dataset/Image'.")

# --- TAMPILKAN HASIL PREDIKSI ---
elif menu == "Tampilkan Hasil Prediksi":
    st.header("Hasil Prediksi yang Tersimpan")

    if st.session_state['history']:
        history_df = pd.DataFrame(st.session_state['history'])
        st.write("**Tabel Hasil Prediksi:**")
        st.dataframe(history_df)

        # Tambahkan tombol reset riwayat prediksi
        if st.button("Reset Riwayat Prediksi"):
            st.session_state['history'] = []
            st.success("Riwayat prediksi telah di-reset.")

        # Display a summary bar plot
        class_counts = pd.Series([h['Prediksi Kelas'] for h in st.session_state['history']]).value_counts()
        fig, ax = plt.subplots()
        ax.bar(class_counts.index, class_counts.values, color='skyblue')
        ax.set_ylabel("Jumlah Prediksi")
        ax.set_title("Distribusi Kelas dari Hasil Prediksi")
        st.pyplot(fig)
    else:
        st.warning("Belum ada hasil prediksi yang tersimpan.")

# --- SIMPAN DATA/IMAGE ---
elif menu == "Simpan Data/Image":
    st.header("Simpan Data/Image")

    if st.session_state['uploaded_image_paths']:
        st.success("Gambar-gambar telah tersimpan di direktori lokal.")
    else:
        st.warning("Belum ada gambar yang diunggah.")
