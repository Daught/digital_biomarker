# Digital Biomarker Repository

This repository contains resources, code, and documentation for analyzing digital biomarkers, including imaging tasks like breast tumor detection and signal processing tasks like ECG and neural spike detection.

---

## Repository Structure

### Imaging

#### 1. **[Breast Tumor Detection](./Imaging/1_Breast_Tumor_Detection)**
Focuses on breast tumor detection using deep learning and smoothing filters.

##### Contents:
- **Data**:
  - [`AttentionCustomUNet.keras`](./Imaging/1_Breast_Tumor_Detection/data/AttentionCustomUNet.keras): Pretrained model for tumor segmentation.
  - [`breast_cancer_prediction.ipynb`](./Imaging/1_Breast_Tumor_Detection/breast_cancer_prediction.ipynb): Notebook for breast cancer prediction.
  - [`breast_ultrasound_cancer_predictions_final.ipynb`](./Imaging/1_Breast_Tumor_Detection/breast_ultrasound_cancer_predictions_final.ipynb): Finalized pipeline for breast cancer predictions.

---

#### 2. **[Smoothing Filters](./Imaging/2_Smoothing_Filters)**
Includes scripts for applying smoothing filters and extracting edges.

##### Contents:
- **Scripts**:
  - [`apply_smoothing_filter.py`](./Imaging/2_Smoothing_Filters/apply_smoothing_filter.py): Script for applying smoothing filters to images.
  - [`extract_edges.py`](./Imaging/2_Smoothing_Filters/extract_edges.py): Script for edge extraction.
  - [`Filtering_template.py`](./Imaging/2_Smoothing_Filters/Filtering_template.py): Template for custom image filtering.
- **Resources**:
  - [`octagon.png`](./Imaging/2_Smoothing_Filters/octagon.png): Sample image for filtering.
  - [`octagon_texture.png`](./Imaging/2_Smoothing_Filters/octagon_texture.png): Textured sample image.

---

#### 3. **[Feature Importance](./Imaging/3_Feature_Importance)**
Focuses on assessing the importance of different features in imaging tasks.

---

### Signals

#### 1. **[ECG and Respiration](./Signals/1_ECG_and_Respiration)**
Contains resources and code for analyzing ECG signals and respiration-related biomarkers.

##### Contents:
- **`ressources/`**: Supporting resources such as CSV data and PDFs.
  - [`apnea-ecg-a01er-data.csv`](./Signals/1_ECG_and_Respiration/ressources/apnea-ecg-a01er-data.csv): ECG data for apnea detection.
  - [`dbm-L1-ecg-RR-interval.pdf`](./Signals/1_ECG_and_Respiration/ressources/dbm-L1-ecg-RR-interval.pdf): Documentation on RR-interval calculations.
- **Jupyter Notebooks**:
  - [`L1-ecg-RR-intervals.ipynb`](./Signals/1_ECG_and_Respiration/L1-ecg-RR-intervals.ipynb): Notebook for RR-interval analysis in ECG signals.

---

#### 2. **[Moving Average Filters on ECGs](./Signals/2_MA_Filters_on_ECGs)**
Implements moving average filters for ECG preprocessing.

##### Contents:
- **Resources**:
  - [`dbm-L2-Moving-Average-Filters.pdf`](./Signals/2_MA_Filters_on_ECGs/dbm-L2-Moving-Average-Filters.pdf): Explanation of moving average filtering for ECGs.
- **Templates**:
  - [`L2-moving-average-filter-ecg-Template.py`](./Signals/2_MA_Filters_on_ECGs/L2-moving-average-filter-ecg-Template.py): Template code for applying moving average filters.
- **Jupyter Notebooks**:
  - [`L2-moving-average-filter-ecg.ipynb`](./Signals/2_MA_Filters_on_ECGs/L2-moving-average-filter-ecg.ipynb): Implementation of moving average filtering.
- **Data**:
  - [`SECG3_FILT_HP51_3CH_20S_FS2400HZ.csv`](./Signals/2_MA_Filters_on_ECGs/SECG3_FILT_HP51_3CH_20S_FS2400HZ.csv): Filtered ECG dataset.

---

#### 3. **[IIR Filters](./Signals/3_IIR_Filters)**
Covers the use of Infinite Impulse Response (IIR) filters for ECG data preprocessing.

##### Contents:
- **Resources**:
  - [`dbm-L3-IIR-Filters.pdf`](./Signals/3_IIR_Filters/dbm-L3-IIR-Filters.pdf): Documentation on IIR filtering.
- **Jupyter Notebooks**:
  - [`L3-IIR-Filters-ecg.ipynb`](./Signals/3_IIR_Filters/L3-IIR-Filters-ecg.ipynb): Notebook implementing IIR filters on ECG signals.
- **Data**:
  - [`SECG3_RAW_3CH_20S_FS2400HZ.csv`](./Signals/3_IIR_Filters/SECG3_RAW_3CH_20S_FS2400HZ.csv): Raw ECG dataset for applying IIR filters.

---

#### 4. **[Neural Spike Detection](./Signals/4_Neural_spike_detection)**
Focuses on detecting neural spikes in recorded signals.

##### Contents:
- **Subdirectories**:
  - [`csv/`](./Signals/4_Neural_spike_detection/csv): Contains datasets for neural spike detection.
  - [`figs-out/`](./Signals/4_Neural_spike_detection/figs-out): Stores output figures from spike detection notebooks.
- **Jupyter Notebooks**:
  - [`ex4-neural-spike-detection.ipynb`](./Signals/4_Neural_spike_detection/ex4-neural-spike-detection.ipynb): Implementation of neural spike detection methods.
  - [`ex4-neural-spike-sorting.ipynb`](./Signals/4_Neural_spike_detection/ex4-neural-spike-sorting.ipynb): Sorting detected spikes into neuronal clusters.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd DIGITAL_BIOMARKER
   ```

2. Explore the subdirectories for different topics (e.g., imaging tasks, ECG analysis, filtering, and neural spike detection).

3. Open Jupyter notebooks in your environment to run and modify the analyses.

---

## Resources
- **Data**: Preprocessed and raw datasets for imaging and signal analysis.
- **Documentation**: PDFs explaining the theoretical background of various filtering techniques and detection methods.
- **Python Code**: Templates and notebooks for applying filters, detecting spikes, and analyzing images.

---

## Results
- Output figures and results for neural spike detection are stored in [`Signals/4_Neural_spike_detection/figs-out/`](./Signals/4_Neural_spike_detection/figs-out).

---

## Acknowledgments
This repository is organized for the study and application of digital biomarkers, focusing on imaging and signal processing tasks.

