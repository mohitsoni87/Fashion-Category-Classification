# Fashion MNIST Model Training and Hyperparameter Tuning

This Jupyter notebook demonstrates the training of Convolutional Neural Networks (CNN) and Feedforward Neural Networks (FNN) on the Fashion MNIST dataset using TensorFlow and Keras. Additionally, it leverages the Keras Tuner library for hyperparameter optimization using Bayesian Optimization.

## Table of Contents
1. [Installation](#installation)
2. [Imports](#imports)
3. [Data Loading and Preprocessing](#data-loading-and-preprocessing)
4. [Constants and TensorBoard Setup](#constants-and-tensorboard-setup)
5. [Model Builders](#model-builders)
6. [Hyperparameter Tuning](#hyperparameter-tuning)
7. [Model Evaluation and Selection](#model-evaluation-and-selection)
8. [Saving the Best Model](#saving-the-best-model)

## Installation
To run this notebook, you need to install the `keras-tuner` library. You can install it using the following command:

```bash
pip install keras-tuner
```

## Imports
The notebook requires several libraries including TensorFlow, Keras utilities, and Keras Tuner for hyperparameter optimization.

## Data Loading and Preprocessing
The Fashion MNIST dataset is loaded and preprocessed:
•	The dataset is reshaped and normalized.
•	Labels are converted to categorical format.


## Constants and TensorBoard Setup
Constants for model training, such as input shape, batch size, epochs, and log directories for TensorBoard, are defined. TensorBoard callbacks are set up for monitoring the training process.

## Model Builders
Two model builder functions are defined:
•	build_simple_cnn: Builds a simple Convolutional Neural Network (CNN).
•	build_feedforward_nn: Builds a Feedforward Neural Network (FNN).

## Hyperparameter Tuning
The notebook uses the Bayesian Optimization tuner from Keras Tuner to find the optimal hyperparameters for both CNN and FNN models. The tuning process involves:
•	Defining the search space for hyperparameters.
•	Running the tuner to search for the best hyperparameters based on validation accuracy.

## Model Evaluation and Selection
The best models from both CNN and FNN tuners are evaluated on the test set. The model with the higher validation accuracy is selected as the better model.

## Saving the Best Model
The best model is saved to the disk for future use.
How to Run the Notebook
1.	Install the required libraries.
2.	Run each cell in the notebook sequentially.
3.	Monitor the training process using TensorBoard.
4.	After training, the best model will be saved automatically.
   
## Note
The notebook includes detailed markdown cells explaining each step, making it easier to follow along and understand the process of model training and hyperparameter tuning.
Acknowledgements
•	TensorFlow and Keras for providing the deep learning framework.
•	Keras Tuner for enabling easy and efficient hyperparameter tuning.
•	Fashion MNIST dataset for the data used in this notebook.


For any questions or issues, please open an issue in this repository.
