import requests
import streamlit as st
import io

def main():
    st.title("Dog or Cat Image Classifier")
    st.write("Upload an image and the classifier will predict whether it's a dog or a cat.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = uploaded_file.read()
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        if st.button('Predict'):
            image_bytes = io.BytesIO(image)  # Convert to bytes
            response = requests.post('http://localhost:8080/predict', files={'image': image_bytes})
            result = response.json()

            if result:
                prediction = result[0]['image']
                st.success(f"The predicted animal is {prediction}.")

if __name__ == '__main__':
    main()