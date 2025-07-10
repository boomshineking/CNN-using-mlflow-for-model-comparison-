import mlflow.pyfunc
import numpy as np
from PIL import Image
import gradio as gr

# 1. Load your model from MLflow
# Replace the run_id below with your actual Run ID
RUN_ID = "3cf8b6a2c1d94699bc1da91cd4a577f6"
model = mlflow.pyfunc.load_model(f"runs:/{RUN_ID}/model")

# 2. Define CIFAR-10 class names
CLASS_NAMES = [
    "airplane","automobile","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

# 3. Prediction function
def predict(img: Image.Image):
    # Resize & normalize exactly like your preprocess pipeline
    img = img.resize((32, 32))
    arr = np.array(img).astype(np.float32) / 255.0    # shape (32,32,3)
    batch = arr[np.newaxis, ...]                     # shape (1,32,32,3)

    # Model returns probabilities for 10 classes
    probs = model.predict(batch)[0]                  # shape (10,)
    
    # Return a label-to-prob dict for Gradio’s Label output
    return {CLASS_NAMES[i]: float(probs[i]) for i in range(10)}

# 4. Build Gradio Interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload a CIFAR-10 image"),
    outputs=gr.Label(num_top_classes=3, label="Predicted Class"),
    title="CIFAR-10 Classifier",
    description="Upload a 32×32 image and see the top-3 CIFAR-10 predictions."
)

if __name__ == "__main__":
    demo.launch()
