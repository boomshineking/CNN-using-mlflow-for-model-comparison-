import os
import tensorflow_datasets as tfds

def download_cifar10(data_dir: str):
    """
    Download the CIFAR-10 dataset into `data_dir` using TFDS.
    """
    os.makedirs(data_dir, exist_ok=True)
    tfds.load(
        name="cifar10",
        data_dir=data_dir,
        download=True
    )

if __name__ == "__main__":
    download_cifar10(data_dir="data/raw")
    print("CIFAR-10 downloaded to data/raw")
