# Dog vs Cat Classification using CNN

This repository contains a Convolutional Neural Network (CNN) model to classify images of dogs and cats. The project includes a web interface built with Streamlit to allow users to upload an image and get a prediction.

## Prerequisites

Ensure you have the following installed on your machine:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/dog-vs-cat-classification-using-cnn.git
    cd dog-vs-cat-classification-using-cnn
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Model

Ensure the trained model `catdogclassifier_final.h5` is in the `models` directory. If the `models` directory does not exist, create it and place the model file inside.

## Running the App

To run the Streamlit app locally, use the following command:

```sh
streamlit run app.py
```

## Usage
Open the app in your web browser.
Use the file uploader to upload an image of a dog or a cat.
The app will display the image and show the predicted class (dog or cat).


/dog-vs-cat-classification-using-cnn
├── app.py
├── requirements.txt
├── models/
│   └── catdogclassifier_final.h5
└── README.md

## Troubleshooting
FileNotFoundError: Ensure that the model file catdogclassifier_final.h5 exists in the models directory and that the path is correct.
ModuleNotFoundError: Make sure all dependencies are installed by running pip install -r requirements.txt.

