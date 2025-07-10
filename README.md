
# CIFAR-10 Image Classification with CNN

This repository contains a complete pipeline for training, evaluating, and deploying a Convolutional Neural Network (CNN) on the CIFAR-10 dataset. It includes data preprocessing, model training with MLflow tracking, and a Gradio web app for interactive inference.

---

## Project Structure

```
.
├── app_gradio.py           # Gradio web app for model inference
├── train.py                # Model training script with MLflow tracking
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables (optional)
├── configs/                # Configuration files (e.g., default.yaml)
├── data/
│   ├── raw/                # Raw CIFAR-10 data
│   └── processed/          # Processed data (if applicable)
├── mlruns/                 # MLflow experiment tracking logs and models
├── notebooks/              # Jupyter notebooks for exploration
├── src/
│   └── data_ingestion/
│       ├── download.py     # Data download utilities
│       └── preprocess.py   # Data preprocessing functions
└── .gradio/                # Gradio app logs and flagged data
```

---

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Data

- The CIFAR-10 dataset is expected in `data/raw/cifar10/`.
- Use scripts in `src/data_ingestion/` to download and preprocess data if not already present.

### 3. Train the Model

```bash
python train.py
```
- Trains a CNN on CIFAR-10.
- Tracks experiments and metrics using MLflow.
- Model artifacts are saved in the `mlruns/` directory.

### 4. Launch the Gradio Web App

```bash
python app_gradio.py
```
- Opens a web interface for uploading images and viewing model predictions.

---

## Key Components

- **Model Training:**  
  See [`train.py`](train.py) for model definition, training loop, and MLflow integration.

- **Data Preprocessing:**  
  Handled in [`src/data_ingestion/preprocess.py`](src/data_ingestion/preprocess.py).

- **Gradio App:**  
  See [`app_gradio.py`](app_gradio.py) for the interactive demo using the trained model.

- **Experiment Tracking:**  
  MLflow logs parameters, metrics, and models. Launch the MLflow UI with:
  ```bash
  mlflow ui
  ```

---

## Requirements

- Python 3.7+
- TensorFlow
- MLflow
- Gradio
- NumPy
- Pillow

(See [`requirements.txt`](requirements.txt) for the full list.)

---

## Acknowledgements

- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [TensorFlow](https://www.tensorflow.org/)
- [MLflow](https://mlflow.org/)
- [Gradio](https://gradio.app/)

---

## License

This project is licensed under the MIT License.
```
