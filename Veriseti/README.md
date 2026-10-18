# Dataset guide

Original paths and filenames are preserved. `HASTALIKLI` is the original disease/contamination category and `NORMAL` is the original normal category. Labels follow the experimental screening described in the report.

## Spectral CSV files

`İNCİR_Birleşik/Ref+Abs_csv/` contains 720 files per class: 360 `_a.csv` absorbance spectra and 360 `_r.csv` reflectance spectra. In total there are 720 paired scan identifiers across the two classes. Each file has 228 numeric data rows. Every absorbance/reflectance pair has a matching wavelength grid.

| Suffix | Actual CSV header |
| --- | --- |
| `_a.csv` | `Wavelength (nm),Absorbance (AU)` |
| `_r.csv` | `Wavelength (nm),Reflectance (AU)` |

The reflectance unit label above is preserved exactly as it appears in the source CSV header. CSVs are not Excel workbooks.

## Image folders

- `kuru_incir/ORİJİNAL` contains **PNG images**, despite its original-folder name; the numeric CSV spectra are located in the paired-CSV folder above.
- `kuru_incir/TEMİZ_GRAFİK` contains several resolution variants and a `REFLACTANCE_512` representation. The original spelling is retained.
- `224_stem` and `256_stem` are alternate plotted representations.
- `500_VERİ_GRAFİK_512` has 500 images per class; `200_TEST_VERİ_GRAFİK_512` has 200 per class. These are original folder labels, not a newly verified split.
- `512-HASTALIKLI`, `512-NORMAL` and `60_448` are additional experimental folders. The `60_448/SİLİNDİ` archive is retained and should not be silently included as active training data.
- `İNCİR_Birleşik/Birlesik_goruntu` contains combined spectral-image representations, with 360 images per class.

Multiple versions can depict the same underlying measurement. Do not treat all 10,726 PNG files as independent physical samples or combine every folder into one training set.

## Actual folder inventory

| Directory | Files | PNG dimensions actually observed |
| --- | ---: | --- |
| `kuru_incir/200_TEST_VERİ_GRAFİK_512/HASTALIKLI` | 200 | 512x512 (200) |
| `kuru_incir/200_TEST_VERİ_GRAFİK_512/NORMAL` | 200 | 512x512 (200) |
| `kuru_incir/224_stem/HASTALIKLI` | 360 | 224x224 (360) |
| `kuru_incir/224_stem/NORMAL` | 360 | 224x224 (360) |
| `kuru_incir/256_stem/HASTALIKLI` | 360 | 256x256 (360) |
| `kuru_incir/256_stem/NORMAL` | 360 | 256x256 (360) |
| `kuru_incir/500_VERİ_GRAFİK_512/HASTALIKLI` | 500 | 512x512 (500) |
| `kuru_incir/500_VERİ_GRAFİK_512/NORMAL` | 500 | 512x512 (500) |
| `kuru_incir/512-HASTALIKLI` | 200 | 512x512 (200) |
| `kuru_incir/512-NORMAL` | 200 | 512x512 (200) |
| `kuru_incir/60_448/GRİDLİ_HASTALIKLI` | 80 | 875x656 (80) |
| `kuru_incir/60_448/GRİDLİ_NORMAL` | 80 | 875x656 (80) |
| `kuru_incir/60_448/SİLİNDİ/GRİDLİ_HASTALIKLI_SİLİNDİ` | 63 | 875x656 (63) |
| `kuru_incir/60_448/SİLİNDİ/GRİDLİ_NORMAL_SİLİNDİ` | 63 | 875x656 (63) |
| `kuru_incir/ORİJİNAL/HASTALIKLI` | 360 | 875x656 (360) |
| `kuru_incir/ORİJİNAL/NORMAL` | 360 | 875x656 (360) |
| `kuru_incir/TEMİZ_GRAFİK/1024/HASTALIKLI` | 360 | 1024x1024 (360) |
| `kuru_incir/TEMİZ_GRAFİK/1024/NORMAL` | 360 | 1024x1024 (360) |
| `kuru_incir/TEMİZ_GRAFİK/224/HASTALIKLI` | 360 | 224x224 (360) |
| `kuru_incir/TEMİZ_GRAFİK/224/NORMAL` | 360 | 224x224 (360) |
| `kuru_incir/TEMİZ_GRAFİK/256/HASTALIKLI` | 360 | 256x256 (360) |
| `kuru_incir/TEMİZ_GRAFİK/256/NORMAL` | 360 | 256x256 (360) |
| `kuru_incir/TEMİZ_GRAFİK/3072/HASTALIKLI` | 360 | 3072x3072 (360) |
| `kuru_incir/TEMİZ_GRAFİK/3072/NORMAL` | 360 | 3072x3072 (360) |
| `kuru_incir/TEMİZ_GRAFİK/400/HASTALIKLI` | 360 | 400x400 (360) |
| `kuru_incir/TEMİZ_GRAFİK/400/NORMAL` | 360 | 400x400 (360) |
| `kuru_incir/TEMİZ_GRAFİK/512/HASTALIKLI` | 360 | 512x512 (360) |
| `kuru_incir/TEMİZ_GRAFİK/512/NORMAL` | 360 | 512x512 (360) |
| `kuru_incir/TEMİZ_GRAFİK/768/HASTALIKLI` | 360 | 768x768 (360) |
| `kuru_incir/TEMİZ_GRAFİK/768/NORMAL` | 360 | 512x512 (34), 768x768 (326) |
| `kuru_incir/TEMİZ_GRAFİK/REFLACTANCE_512/HASTALIKLI` | 360 | 512x512 (360) |
| `kuru_incir/TEMİZ_GRAFİK/REFLACTANCE_512/NORMAL` | 360 | 512x512 (360) |
| `İNCİR_Birleşik/Birlesik_goruntu/HASTALIKLI` | 360 | 640x480 (360) |
| `İNCİR_Birleşik/Birlesik_goruntu/NORMAL` | 360 | 640x480 (360) |
| `İNCİR_Birleşik/Ref+Abs_csv/HASTALIKLI` | 720 | CSV spectra |
| `İNCİR_Birleşik/Ref+Abs_csv/NORMAL` | 720 | CSV spectra |

Dimensions are measured from PNG headers; a folder name alone is not used to infer image size. Machine-readable counts are in [`../docs/dataset_inventory.json`](../docs/dataset_inventory.json). See [`../docs/reproducibility.md`](../docs/reproducibility.md) for validation scope and experiment limitations.
