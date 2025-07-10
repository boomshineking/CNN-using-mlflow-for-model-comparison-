
# CIFAR-10 Image Classification with CNN
                    '''Please do note i have not upload all the parts of project structure as most of it is generated during work once you run test.py you will generate mlruns and artifact'''
This repository contains a complete pipeline for training, evaluating, and deploying a Convolutional Neural Network (CNN) on the CIFAR-10 dataset. It includes data preprocessing, model training with MLflow tracking, and a Gradio web app for interactive inference.

---

## Project Structure

```
.
├── app_gradio.py           # Gradio web app for model inference
├── train.py                # Model training script with MLflow tracking
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables was just for my own experimentation no need for it 
├── configs/                # Configuration files (e.g., default.yaml)
├── data/                   # Could not upload data folder due to size of the file too long to upload
│   ├── raw/                # Raw CIFAR-10 data
│   └── processed/          # Processed data (if applicable for experimentation)
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

- Python 3.10
- TensorFlow
- MLflow
- Gradio
- NumPy
- Pillow

(See [`requirements.txt`](requirements.txt) for the full list.)

---
## Screenshot of deployement on gradio 

<img width="936" height="915" alt="Screenshot 2025-07-10 012403" src="https://github.com/user-attachments/assets/89d36a0f-231b-477a-aa8b-c556fe2693ac" />
<img width="950" height="916" alt="Screenshot 2025-07-10 012808" src="https://github.com/user-attachments/assets/7982a47c-c112-4690-ac39-b32048520e81" />

## Screenshot of Mlflow works

<img width="1869" height="922" alt="Screenshot 2025-07-10 004305" src="https://github.com/user-attachments/assets/96a2f038-8e34-47b1-b0f2-7bda03a53f38" />

<img width="1919" height="1079" alt="Screenshot 2025-07-10 003234" src="https://github.com/user-attachments/assets/a01e569d-f115-44ec-a737-fac4e0bfce01" 
  
<img width="1869" height="922" alt="mlflowcharts" src="https://github.com/user-attachments/assets/2a30c9f2-9c6b-4381-8d9c-61a4f0b6c503" />

## Acknowledgements

- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [TensorFlow](https://www.tensorflow.org/)
- [MLflow](https://mlflow.org/)
- [Gradio](https://gradio.app/)

---

## License

This project is licensed under the MIT License.
```
