import os
from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageOps

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MODEL_PATH'] = 'saved_model/cnn_model'

# Load your TensorFlow model
model = tf.saved_model.load(app.config['MODEL_PATH'])

# Mapping from class index to class name
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# Function to preprocess image for prediction
def preprocess_image(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale

    # Convert image to RGBA to handle transparency
    img = image.convert('RGBA')
    # Create a new image with a black background
    background = Image.new('RGBA', img.size, (0, 0, 0, 255))
    # Paste the original image onto the black background
    background.paste(img, (0, 0), img)
    # Convert to grayscale
    gray_img = ImageOps.grayscale(background)
    # Resize the image to 28x28 pixels (the size of images in the Fashion MNIST dataset)
    image = gray_img.resize((28, 28))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the image data to [0, 1] range
    image_array = image_array.astype('float32') / 255.0

    # Add the channel dimension (since it's a grayscale image, the channel dimension is 1)
    image_array = np.expand_dims(image_array, axis=-1)  # Shape should be (28, 28, 1)

    # Add the batch dimension
    image_array = np.expand_dims(image_array, axis=0)  # Shape should be (1, 28, 28, 1)

    transformedImage(image_array, image_path)
    return image_array
'''
    # Load the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the image data to [0, 1] range
    image_array = image_array.astype('float32') / 255.0

    # Add the channel dimension (since it's a grayscale image, the channel dimension is 1)
    image_array = np.expand_dims(image_array, axis=-1)  # Shape should be (28, 28, 1)

    # Add the batch dimension
    image_array = np.expand_dims(image_array, axis=0)  # Shape should be (1, 28, 28, 1)

    return image_array'''

def transformedImage(image_array, image_path):
    # Remove the batch and channel dimensions for saving
    image_array_to_save = np.squeeze(image_array, axis=0)  # Shape is now (28, 28, 1)
    image_array_to_save = np.squeeze(image_array_to_save, axis=-1)  # Shape is now (28, 28)

    # Convert the normalized image data back to the [0, 255] range
    image_array_to_save = (image_array_to_save * 255).astype('uint8')

    # Convert the NumPy array back to a PIL image
    processed_image = Image.fromarray(image_array_to_save)

    # Save the image
    directory, base_name = os.path.split(image_path)
    name, ext = os.path.splitext(base_name)
    new_name = f"{name}_transformed{ext}"
    new_path = os.path.join(directory, new_name)

    processed_image.save(new_path)

# Function to perform prediction
def predict(img_array):
    predictions = model(img_array)
    return predictions

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Save the uploaded image to uploads folder
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(img_path)
            img_array = preprocess_image(img_path)
            # Perform prediction
            preds = predict(img_array)
            predicted_class = np.argmax(preds[0])
            predicted_label = 'The uploaded image is a ' + class_names[predicted_class]
            image_url = url_for('static', filename='uploads/' + file.filename)
            return render_template('index.html', prediction=predicted_label, image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)
