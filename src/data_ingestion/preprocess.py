import tensorflow as tf
import tensorflow_datasets as tfds

def normalize_img(image, label):
    """
    Cast image to float32 in [0,1].
    """
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

def load_and_preprocess(data_dir: str, batch_size: int = 32):
    """
    Load CIFAR-10 from `data_dir`, normalize, batch, and prefetch.
    Returns (train_ds, test_ds).
    """
    # as_supervised yields (image, label) tuples
    ds_train, ds_test = tfds.load(
        "cifar10",
        split=["train", "test"],
        data_dir=data_dir,
        as_supervised=True
    )

    ds_train = (
        ds_train
        .map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
        .cache()
        .shuffle(10_000)
        .batch(batch_size)
        .prefetch(tf.data.AUTOTUNE)
    )

    ds_test = (
        ds_test
        .map(normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
        .batch(batch_size)
        .prefetch(tf.data.AUTOTUNE)
    )

    return ds_train, ds_test

if __name__ == "__main__":
    train_ds, test_ds = load_and_preprocess(data_dir="data/raw")
    print(f"Train batches: {len(list(train_ds))}, Test batches: {len(list(test_ds))}")
