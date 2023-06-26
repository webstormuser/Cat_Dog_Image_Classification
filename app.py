import streamlit as st
import os
from com_in_ineuron_ai_utils.utils import decodeImage
from prediction.predict import DogCat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DogCat(self.filename)


clApp = ClientApp()

def predict(image):
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return result

def main():
    st.title("Dog Cat Image Classification")
    image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if image is not None:
        st.image(image, caption="Uploaded Image", use_column_width=True)
        result = predict(image)
        st.write("Prediction Result:", result)

if __name__ == "__main__":
    main()