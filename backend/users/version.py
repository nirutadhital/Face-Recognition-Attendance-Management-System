# import tensorflow as tf
# print("TensorFlow Version:", tf.__version__)
# print("Keras Version:", tf.keras.__version__)

# from tensorflow.keras.models import load_model, save_model

# # Load the model
# model = load_model('facenet_keras.h5')

# # Re-save the model in the legacy H5 format
# save_model(model, 'facenet_keras_updated.h5', save_format='h5')

# import os
# import h5py
# from keras.api.models import load_model, save_model, model_from_json

# # Step 1: Load the model
# try:
#     model = load_model('facenet_keras.h5')
# except Exception as e:
#     print(f"Error loading model: {e}")
#     print("Attempting to rebuild the model...")
    
#     # Step 2: Extract model configuration and weights
#     with h5py.File('facenet_keras.h5', 'r') as f:
#         model_config = f.attrs.get('model_config')
#         model_weights = [layer for layer in f['model_weights']]
    
#     # Step 3: Rebuild the model
#     model = model_from_json(model_config)
#     model.load_weights('facenet_keras.h5')

# # Step 4: Re-save the model
# save_model(model, 'facenet_keras_v2.h5')
# print("Model re-saved successfully!")

# # Step 5: Verify the re-saved model
# new_model = load_model('facenet_keras_v2.h5')
# print("Re-saved model loaded successfully!")


# import h5py
# import keras

# model_path = "facenet_keras.h5"  # Replace with your model path
# with h5py.File(model_path, 'r') as f:
#     print(f.attrs.get("keras_version"))
#     print(f.attrs.get("backend"))


# from keras.api.models import load_model
# model = load_model("facenet_keras.h5")
# model.save("facenet_tf", save_format="tf")

# from tensorflow.python.keras.models import load_model
# # from keras.api.layers import BatchNormalization
# from keras.api.layers import BatchNormalization
# from tensorflow.python.keras.layers import VersionAwareLayers  # Import VersionAwareLayers

# # Create an instance of VersionAwareLayers
# layers = VersionAwareLayers()

# # Define custom_objects dictionary with version-aware BatchNormalization
# custom_objects = {
#     'BatchNormalization': layers.BatchNormalization  # Use version-aware BatchNormalization
# }

# # Load the model with custom_objects
# try:
#     model = load_model('facenet_keras.h5', custom_objects=custom_objects)
# except Exception as e:
#     print(f"Error loading model: {e}")


from tensorflow.python.keras.models import load_model
from tensorflow.keras.layers import BatchNormalization  # Import the layer

# Define custom_objects dictionary
custom_objects = {
    'BatchNormalization': BatchNormalization  # Add any other custom layers here
}

# Load the model with custom_objects
try:
    model = load_model('facenet_keras.h5', custom_objects=custom_objects)
except Exception as e:
    print(f"Error loading model: {e}")









