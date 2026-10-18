# NIR-Based Classification of Dried Figs

**2024 graduation project — Emre Öztürk, Electrical and Electronics Engineering, Yeditepe University.**

Supervisor: Asst. Prof. Dr. İpek Baz.

This repository archives the project **“Detection of mycotoxins in dry fig using NIR scan with AI-based methods.”** It contains the original report, two presentations, NIR spectral CSV files, derived spectral images, and MATLAB/Python listings transcribed from the report appendices.

The work investigates classification of dried-fig measurements into the original `HASTALIKLI` and `NORMAL` categories using spectral plots and a convolutional neural network. The report describes UV-based screening of the supplied fig samples. The labels should be read in that experimental context; the repository does not supply laboratory toxin-concentration measurements or establish a quantitative toxin assay.

## Contents

| Location | Contents |
| --- | --- |
| [`Veriseti/`](Veriseti/README.md) | Original directory hierarchy: 1,440 CSV files and 10,726 PNG files, including multiple representations and experimental variants. |
| [`results/`](results/README.md) | Learning curves, all-attempt result table, and original Colab/Raspberry Pi evaluation screenshots. |
| [`code/report_appendices/`](code/README.md) | Five historical MATLAB/Python code listings extracted from appendices A–E of the report. |
| [Project report](EE492_PROJECT%20REPORT%20_O.EMRE_24SP.docx) | Original 2024 DOCX report, including methods, experimental results, references and code appendices. |
| [PPTX presentation](EE492_PROJECT%20PRESENTATION%20_O.EMRE_.pptx) | Original presentation. |
| [PPT presentation](EE492_PROJECT%20PRESENTATION_E.OZTURK_24SP.ppt) | Original legacy PowerPoint presentation. |
| [`docs/dataset_inventory.json`](docs/dataset_inventory.json) | Actual file counts, image dimensions, CSV properties and extracted-code checks. |
| [`docs/source_manifest.json`](docs/source_manifest.json) | Relative paths, sizes and SHA-256 checksums for all 12,169 original source files. |
| [`docs/reproducibility.md`](docs/reproducibility.md) | Reproduction status and limitations of the archived material. |

## Dataset at a glance

- Original source material: **12,169 files, 195,344,830 bytes**; documentation and extracted code are additional files.
- CSV spectra: **720 absorbance/reflectance pairs** — 360 pairs per original class.
- Each CSV contains **228 numeric wavelength/signal rows**, with wavelength grids spanning approximately **901.66–1700.71 nm**.
- PNG files include different resolutions, plot styles, combined absorbance/reflectance images and separate experiment folders. They are **not 10,726 independent physical samples**.
- All original filenames and file contents are retained. See the [dataset guide](Veriseti/README.md) before selecting an experiment folder.

## Reported results

Browse the [results archive](results/README.md) for the original learning curves, Table 3, and evaluation screenshots.

The report describes the selected “Attempt-8” model as achieving **97.79% training accuracy** and **82% accuracy on a separate 400-image evaluation**, with reported evaluation loss **0.48**. These are historical results reported in the document; training and evaluation were not rerun for this upload. Training accuracy should not be presented as held-out test accuracy.

## Code and reproduction status

The supplied folder did not contain standalone source files or saved model weights. The code now available under `code/report_appendices/` is a text transcription of the original report listings, with provenance comments added.

**The historical training listing contains syntax and variable-name inconsistencies and is not a verified runnable training pipeline.** Colab/Windows paths and dependencies also require adaptation. No `.h5`, `.keras`, notebook, saved split manifest or pinned environment was present in the supplied folder. Details are documented in the [code guide](code/README.md) and [reproducibility notes](docs/reproducibility.md).

## Download

```bash
git clone https://github.com/emreozturk2098/nir-detection-mycotoxins-in-dr-fig.git
cd nir-detection-mycotoxins-in-dr-fig
```

All supplied files are stored directly in Git; this archive does not require Git LFS or split-file reconstruction.

## Attribution and license status

Author and project context are recorded in the original report. References and third-party figure credits remain in the original documents. An explicit reuse license has not been specified for this archive.
