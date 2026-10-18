# Archive provenance and reproduction status

## Preserved source material

The publication preparation copied all 12,169 supplied files without changing their byte content. The original report and presentations remain in their original formats and filenames. Dataset paths, including Turkish characters, experimental folder names and the `SİLİNDİ` subfolder, are preserved.

`source_manifest.json` describes the original source files only. New README files, inventories, Git configuration files and report-derived code listings are additional repository files. The source manifest records SHA-256 checksums, file sizes and source last-write timestamps; it contains relative paths rather than absolute desktop paths.

## Checks performed

- Every copied source file was compared with its source using SHA-256.
- All 1,440 CSV files were parsed as two numeric columns; their 228 data rows contained finite numbers.
- All 720 absorbance files had a corresponding reflectance file with the same wavelength grid.
- PNG signatures and dimensions were read for the inventory. This does not establish that a particular image reproduces a particular CSV exactly.
- The code was extracted from the report text. Three Python listings passed Python syntax parsing; the historical training listing failed syntax parsing. MATLAB and model training were not executed.

## Interpretation of the archive

`HASTALIKLI` and `NORMAL` retain the original class labels. The report describes UV-based screening of the supplied fig samples; no per-sample analytical aflatoxin concentration table was present in this folder.

Multiple PNG folders contain alternative views, resolutions or experiment subsets. Counts across these folders must not be added to obtain a number of independent figs. Before a new evaluation, establish physical-sample grouping, identify repeated scans and derivative images, and define train/validation/test partitions that do not share source measurements or physical samples.

The archive does not include the original model weights, random split membership, a pinned software environment or execution logs that would reproduce the reported scores exactly. The report's selected model is described with 97.79% training accuracy and 82% accuracy on a separate 400-image evaluation; these historical scores were not independently reproduced during publication.

The report also describes class-dependent normalization trials. Those trials should not be treated as a label-independent inference procedure or used to replace the stated 82% held-out result with a higher headline score.

The original Office documents are preserved as historical records; their wording, figures and experimental inconsistencies were not rewritten during this upload.

## Extracted result artifacts

Original report/presentation curves, the embedded result table and evaluation screenshots are available in [`../results/README.md`](../results/README.md). They are historical source artifacts, not outputs of rerunning the code. Complete epoch histories, all prediction/label pairs and model weights remain unavailable, so a full-test confusion matrix cannot be reconstructed from this archive alone.
