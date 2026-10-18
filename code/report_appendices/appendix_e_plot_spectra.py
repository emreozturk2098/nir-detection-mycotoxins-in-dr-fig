# Extracted from Appendix E of the original 2024 project report.
# Historical listing: see code/README.md before use.

import os
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')


# Veri klasörlerini belirt
afla_klasoru = '/content/drive/MyDrive/EXCEL_VERİLERİ_TRAİN/HASTALIKLI'
normal_klasoru = '/content/drive/MyDrive/EXCEL_VERİLERİ_TRAİN/NORMAL'

def cizdir_ve_kaydet(klasor, title, dosya_adi):
    plt.figure(figsize=(10, 6))
    dosyalar = os.listdir(klasor)
    for dosya in dosyalar:
        if dosya.endswith('_a.csv'):
            dosya_yolu = os.path.join(klasor, dosya)
            veri = pd.read_csv(dosya_yolu)
            plt.plot(veri['Wavelength (nm)'], veri['Absorbance (AU)'], label=f'{dosya[:-10]}')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Absorbance (AU)')
    plt.title(title)
    plt.legend(bbox_to_anchor=(1.05, 2), loc='upper left')
    plt.grid(True)
    plt.savefig(dosya_adi, bbox_inches='tight')
    plt.show()
