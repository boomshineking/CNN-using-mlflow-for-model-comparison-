import mlflow
import mlflow.tensorflow
from src.data_ingestion.preprocess import load_and_preprocess
from tensorflow.keras import layers, models

# Enable TensorFlow autologging
mlflow.tensorflow.autolog()

def build_cnn(input_shape=(32, 32, 3), num_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, 3, padding='same', activation='relu',
                      input_shape=input_shape),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax'),
    ])
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

if __name__ == "__main__":
    # Load preprocessed data
    train_ds, test_ds = load_and_preprocess(data_dir="data/raw", batch_size=32)

    # Set up MLflow experiment
    mlflow.set_experiment("cifar10-cnn")

    # Start MLflow run
    with mlflow.start_run(run_name="e20increase"):
        model = build_cnn()
        model.fit(
            train_ds,
            epochs=20,
            validation_data=test_ds
        )
        # Log final test accuracy manually
        loss, acc = model.evaluate(test_ds)
        mlflow.log_metric("final_test_accuracy", acc)
