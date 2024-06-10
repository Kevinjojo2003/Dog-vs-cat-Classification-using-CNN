import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

# Load the trained model
model = tf.keras.models.load_model('models/catdogclassifier_final.h5')

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to match the model's expected sizing
    img = cv2.resize(image, (256, 256))
    # Convert image to array and normalize pixel values
    img = np.array(img) / 255.0
    # Expand dimensions to match the input shape of the model
    img = np.expand_dims(img, axis=0)
    return img

# Streamlit app
def main():
    st.title("Cat vs Dog Classification")

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)

        # Display the result
        if prediction > 0.5:
            st.write("Prediction: Dog")
        else:
            st.write("Prediction: Cat")

if __name__ == "__main__":
    main()
