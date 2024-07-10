# CNN Fashion MNIST Web App

This repository contains a web application that classifies fashion items using a Convolutional Neural Network (CNN) trained on the Fashion MNIST dataset. The application allows users to upload images and receive predictions on the type of fashion item depicted.

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project demonstrates how to deploy a trained machine learning model using a Flask web application. The model is a CNN trained on the Fashion MNIST dataset, which consists of grayscale images of various clothing items. Users can interact with the web app by uploading images and receiving predictions.



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cnn-fashion-mnist-webapp.git
    cd cnn-fashion-mnist-webapp
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask web application:
    ```bash
    python main.py
    ```

2. Open your browser and navigate to `http://localhost:5000`.

3. Upload an image and receive predictions on the type of fashion item.

## Model Details

The CNN model is trained on the Fashion MNIST dataset, which includes the following classes:

- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle boot

The model files are stored in the `saved_model/cnn_model` directory. The model was trained using TensorFlow and saved in the TensorFlow SavedModel format.

## API Endpoints

The web application provides the following endpoints:

- `GET /`: Home page with image upload form
- `POST /predict`: Endpoint to handle image upload and return predictions

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
