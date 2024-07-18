
# CNN Fashion MNIST Web App

This repository contains a web application that classifies fashion items using a Convolutional Neural Network (CNN) trained on the Fashion MNIST dataset. The application allows users to upload images and receive predictions on the type of fashion item depicted. 

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)

## Project Overview

This project demonstrates how to deploy a trained machine learning model using a Flask web application. The model is a CNN trained on the Fashion MNIST dataset, which consists of grayscale images of various clothing items. Users can interact with the web app by uploading images and receiving predictions.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mohitsoni87/Fashion-Category-Classification
    cd Fashion-Category-Classification
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Start Flask in Local

1. Start the Flask web application:

    ```bash
    python main.py
    ```

2. Open your browser and navigate to `http://localhost:5000`.

3. Upload an image and receive predictions on the type of fashion item.



### Create Docker Image & Deploy Tensorflow Model & Flask App in Local using Docker

1. The Default Dockerfile in the root directory has the docker configuration for Google Cloud.

2. Take a backup of the default Dockerfile. You may rename the file to Dockerfile-GCloud.

3. Rename Dockerfile-Local to Docker file, so that the docker build commands is able to pick up this file.

4. Build the docker image from the root folder of the project.

    ```bash
    docker build -t my-flask-app .
    ```

5. Execute the Docker run command to kickstart the container
    ```bash
    docker run -p 5000:80 my-flask-app
    ```

6. Open your browser and navigate to `http://localhost:5000`.

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
