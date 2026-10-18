# Code extracted from the original report

The supplied project folder contained dataset files and Office documents, but no separate `.py`, `.m`, `.ipynb` or trained-model files. The listings below were transcribed from the text of the original DOCX report. Provenance comments were added; historical algorithms and errors were retained.

| Appendix | File | Purpose | Check performed |
| --- | --- | --- | --- |
| A | [`appendix_a_csv_to_png.m`](report_appendices/appendix_a_csv_to_png.m) | MATLAB CSV-to-PNG spectral plotting. | Extracted; MATLAB execution not tested. |
| B | [`appendix_b_training.py`](report_appendices/appendix_b_training.py) | Colab/TensorFlow image loading, dataset partitioning, CNN training and plots. | Historical syntax error retained; not runnable as supplied. |
| C | [`appendix_c_save_model.py`](report_appendices/appendix_c_save_model.py) | Save a model from the training session. | Python syntax accepted; requires an existing `model` object. |
| D | [`appendix_d_evaluate_model.py`](report_appendices/appendix_d_evaluate_model.py) | Load a saved model and evaluate two image classes. | Python syntax accepted; runtime/model availability not tested. |
| E | [`appendix_e_plot_spectra.py`](report_appendices/appendix_e_plot_spectra.py) | Define a function to plot absorbance CSV spectra. | Python syntax accepted; Colab paths and function invocation require adaptation. |

## Known issues in the historical listings

- Appendix B includes `batch_size= batch _SIZE`, which is invalid Python syntax.
- The same listing mixes `batch_SIZE`, `BATCH_SIZE`, `epochs` and `EPOCHS`, and uses `SHUFFLE = TRUE` instead of the expected Python/Keras argument spelling and boolean.
- Its prediction helper reads the outer variables `images` and `i` instead of using only its `img` parameter.
- Dataset partitions are derived from a shuffled/batched TensorFlow dataset; no original split indices, per-fig grouping or overlap checks are supplied.
- Windows and Google Drive paths refer to the author's historical environment. Some folder names in the code differ from the supplied archive.
- The save-model snippet relies on a preceding training session and does not provide trained model weights. Its comment describes H5 saving while the path itself has no `.h5` suffix; behavior depends on the original Keras version.
- The evaluation listing points to `500_VERİ_GRAFİK_512`; do not assume that this path is the report's separate 400-image test set.

The report mentions MATLAB, Python, TensorFlow/Keras, NumPy, pandas, Matplotlib, scikit-learn and Google Colab. Exact package versions were not supplied. No successful training or model-reproduction claim is made for these extracted listings.
