# Digital Biomarker Repository

This repository contains resources, code, and documentation for analyzing digital biomarkers, including ECG and neural spike detection.

---

## Repository Structure

### 1. **[ECG and Respiration](./1_ECG_and_Respiration)**
Contains resources and code for analyzing ECG signals and respiration-related biomarkers.

#### Contents:
- **`ressources/`**: Supporting resources such as CSV data and PDFs.
  - [`apnea-ecg-a01er-data.csv`](./1_ECG_and_Respiration/ressources/apnea-ecg-a01er-data.csv): ECG data for apnea detection.
  - [`dbm-L1-ecg-RR-interval.pdf`](./1_ECG_and_Respiration/ressources/dbm-L1-ecg-RR-interval.pdf): Documentation on RR-interval calculations.
- **Jupyter Notebooks**:
  - [`L1-ecg-RR-intervals.ipynb`](./1_ECG_and_Respiration/L1-ecg-RR-intervals.ipynb): Notebook for RR-interval analysis in ECG signals.

---

### 2. **[Moving Average Filters on ECGs](./2_MA_Filters_on_ECGs)**
Implements moving average filters for ECG preprocessing.

#### Contents:
- **Resources**:
  - [`dbm-L2-Moving-Average-Filters.pdf`](./2_MA_Filters_on_ECGs/dbm-L2-Moving-Average-Filters.pdf): Explanation of moving average filtering for ECGs.
- **Templates**:
  - [`L2-moving-average-filter-ecg-Template.py`](./2_MA_Filters_on_ECGs/L2-moving-average-filter-ecg-Template.py): Template code for applying moving average filters.
- **Jupyter Notebooks**:
  - [`L2-moving-average-filter-ecg.ipynb`](./2_MA_Filters_on_ECGs/L2-moving-average-filter-ecg.ipynb): Implementation of moving average filtering.
- **Data**:
  - [`SECG3_FILT_HP51_3CH_20S_FS2400HZ.csv`](./2_MA_Filters_on_ECGs/SECG3_FILT_HP51_3CH_20S_FS2400HZ.csv): Filtered ECG dataset.

---

### 3. **[IIR Filters](./3_IIR_Filters)**
Covers the use of Infinite Impulse Response (IIR) filters for ECG data preprocessing.

#### Contents:
- **Resources**:
  - [`dbm-L3-IIR-Filters.pdf`](./3_IIR_Filters/dbm-L3-IIR-Filters.pdf): Documentation on IIR filtering.
- **Jupyter Notebooks**:
  - [`L3-IIR-Filters-ecg.ipynb`](./3_IIR_Filters/L3-IIR-Filters-ecg.ipynb): Notebook implementing IIR filters on ECG signals.
- **Data**:
  - [`SECG3_RAW_3CH_20S_FS2400HZ.csv`](./3_IIR_Filters/SECG3_RAW_3CH_20S_FS2400HZ.csv): Raw ECG dataset for applying IIR filters.

---

### 4. **[Neural Spike Detection](./4_Neural_spike_detection)**
Focuses on detecting neural spikes in recorded signals.

#### Contents:
- **Subdirectories**:
  - [`csv/`](./4_Neural_spike_detection/csv): Contains datasets for neural spike detection.
  - [`figs-out/`](./4_Neural_spike_detection/figs-out): Stores output figures from spike detection notebooks.
- **Jupyter Notebooks**:
  - [`ex4-neural-spike-detection.ipynb`](./4_Neural_spike_detection/ex4-neural-spike-detection.ipynb): Implementation of neural spike detection methods.
  - [`ex4-neural-spike-sorting.ipynb`](./4_Neural_spike_detection/ex4-neural-spike-sorting.ipynb): Sorting detected spikes into neuronal clusters.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd DIGITAL_BIOMARKER
   ```

2. Explore the subdirectories for different topics (e.g., ECG analysis, filtering, and neural spike detection).

3. Open Jupyter notebooks in your environment to run and modify the analyses.

---

## Resources
- **Data**: Preprocessed and raw datasets for ECG and neural spike analysis.
- **Documentation**: PDFs explaining the theoretical background of various filtering techniques and spike detection.
- **Python Code**: Templates and notebooks for applying filters and detecting neural spikes.

---

## Results
- Output figures and results for neural spike detection are stored in [`4_Neural_spike_detection/figs-out/`](./4_Neural_spike_detection/figs-out).

---

## Acknowledgments
This repository is organized for the study and application of digital biomarkers, focusing on preprocessing and analysis of physiological signals.

