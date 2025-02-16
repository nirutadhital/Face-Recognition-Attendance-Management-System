# import h5py

# try:
#     with h5py.File('facenet_keras.h5', 'r') as f:
#         print("File opened successfully.")
#         print("Keys in the file:", list(f.keys()))
# except Exception as e:
#     print(f"Error inspecting .h5 file: {e}")

import h5py

try:
    with h5py.File('facenet_keras.h5', 'r') as f:
        print("File opened successfully.")
        print("Keys in the file:", list(f.keys()))
except Exception as e:
    print(f"Error inspecting .h5 file: {e}")