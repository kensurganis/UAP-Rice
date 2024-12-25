# -*- coding: utf-8 -*-
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.callbacks import EarlyStopping # type: ignore
from tensorflow.keras.callbacks import ModelCheckpoint # type: ignore
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Set seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# Path dataset
BASE_PATH = "C:/Users/MSI-PC/Documents/uap/src/uap/Rice_Image_Dataset"
TRAIN_PATH = os.path.join(BASE_PATH, "train")
TEST_PATH = os.path.join(BASE_PATH, "test")

# Konfigurasi dataset
IMG_HEIGHT, IMG_WIDTH = 128, 128
BATCH_SIZE = 16
EPOCHS = 10
CLASSES = ['Basmati', 'Arborio', 'Ipsala', 'Karacadag', 'Jasmine']

# Data augmentation dan generator
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    TRAIN_PATH,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode="sparse"
)

test_generator = test_datagen.flow_from_directory(
    TEST_PATH,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode="sparse"
)

# Model CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(len(CLASSES), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Summary model
model.summary()

#  EarlyStopping
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# ModelCheckpoint
model_checkpoint = ModelCheckpoint(
    filepath='C:/Users/MSI-PC/Documents/uap/src/uap/model/citra_cnn.keras',  # Gunakan format .h5
    monitor='val_loss',
    save_best_only=True,
    mode='min'
)

# Callback List
callbacks = [early_stopping, model_checkpoint]

# Training model
history = model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=EPOCHS
)

# Plot training history
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

# Evaluasi model
loss, accuracy = model.evaluate(test_generator)
print(f'Test Accuracy: {accuracy:.2f}')
print(f'Test Loss: {loss:.2f}')

# Prediksi dan Confusion Matrix
y_true = []
y_pred = []

for images, labels in test_generator:
    predictions = model.predict(images)
    y_true.extend(labels)
    y_pred.extend(np.argmax(predictions, axis=1))
    if len(y_true) >= test_generator.samples:
        break

y_true = np.array(y_true[:test_generator.samples])
y_pred = np.array(y_pred[:test_generator.samples])

print(classification_report(y_true, y_pred, target_names=CLASSES))

cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=CLASSES)
disp.plot(cmap=plt.cm.Blues, values_format='d')
plt.show()

# Simpan model
model.save("C:/Users/MSI-PC/Documents/uap/src/uap/model/citra_cnn.h5")
print("Model berhasil disimpan ke 'citra_cnn.h5'")