import tensorflow as tf
import numpy as np
from skimage import transform

model = tf.keras.models.load_model('models/cow_disease_detector.h5', compile=False)


def load(image):
    np_image = image
    np_image = np.array(np_image).astype('float32') / 255
    np_image = transform.resize(np_image, (200, 200, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


class CowDiseaseDetector:
    diseases = {0: 'healthy', 1: 'lumpy'}

    def __init__(self):
        self.model = model

    def predict(self, image):
        loaded_image = tf.keras.utils.load_img(image)
        processed_image = load(loaded_image)
        prediction = self.model.predict(processed_image)
        disease_index = prediction.argmax()

        accuracy = (prediction[0][disease_index] / prediction[0].sum()) * 100
        print(f"Accuracy {accuracy}")
        return accuracy, self.diseases[disease_index]
