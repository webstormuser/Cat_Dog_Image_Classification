# predict.py
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class DogCat:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model(os.path.join("model", "model.h5"))

    def predictiondogcat(self, image_path):
        test_image = image.load_img(image_path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(self.model.predict(test_image), axis=1)

        if result[0] == 1:
            prediction = 'dog'
        else:
            prediction = 'cat'

        return [{"image": prediction}]