# Extracted from Appendix D of the original 2024 project report.
# Historical listing: see code/README.md before use.

import os
import numpy as np
from sklearn.metrics import accuracy_score, log_loss
from keras.preprocessing.image import load_img, img_to_array
from keras.utils import to_categorical
from tensorflow.keras.models import load_model

# Aflatoksin ve normal klasörlerinin yolları
afla_klasoru = "/content/drive/MyDrive/kuru_incir/500_VERİ_GRAFİK_512/HASTALIKLI"
normal_klasoru = "/content/drive/MyDrive/kuru_incir/500_VERİ_GRAFİK_512/NORMAL"

# Verileri ve etiketleri depolamak için boş listeler
X = []
y = []

# afla verilerini yükleme ve etiketleme
for dosya_adi in os.listdir(afla_klasoru):
    dosya_yolu = os.path.join(afla_klasoru, dosya_adi)
    img = load_img(dosya_yolu, target_size=(512, 512))
    img_array = img_to_array(img)
    X.append(img_array)
    y.append(0)  # afla sınıfı

# Normal verilerini yükleme ve etiketleme
for dosya_adi in os.listdir(normal_klasoru):
    dosya_yolu = os.path.join(normal_klasoru, dosya_adi)
    img = load_img(dosya_yolu, target_size=(512, 512))
    img_array = img_to_array(img)
    X.append(img_array)
    y.append(1)  # Normal sınıfı

# Veriyi ve etiketleri Numpy dizilerine dönüştürme
X = np.array(X)
y = np.array(y)

# Verileri karıştırma
sirali_indeksler = np.arange(X.shape[0])
np.random.shuffle(sirali_indeksler)
X = X[sirali_indeksler]
y = y[sirali_indeksler]

# Modeli yükleyip verileri tahmin etme
model = load_model('/content/drive/MyDrive/kuru_incir/H5_dosyası_GORUNMEYEN_TEST')  # Kaydedilmiş modeli yükleme
predictions = model.predict(X)  # Verileri tahmin etme

# Gerçek etiketlerin ve tahminlerin hazırlanması
true_labels = y
true_labels_cat = to_categorical(true_labels, num_classes=2)  # Gerçek etiketlerin kategorik hale getirilmesi
pred_prob_cat = predictions  # Tahmin olasılıklarının hesaplanması

# Doğruluk oranını ve kaybı hesaplama
accuracy = accuracy_score(true_labels, np.argmax(predictions, axis=1))
loss = log_loss(true_labels_cat, pred_prob_cat)

print(f"Doğruluk Oranı: {accuracy}")
print(f"Kayıp: {loss}")
