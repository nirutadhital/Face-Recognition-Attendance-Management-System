# import h5py

# try:
#     with h5py.File('facenet_keras.h5', 'r') as f:
#         print("File opened successfully.")
#         print("Keys in the file:", list(f.keys()))
# except Exception as e:
#     print(f"Error inspecting .h5 file: {e}")

# import cv2

# stream_url = "http://192.168.72.32:8080/video"
# video_capture = cv2.VideoCapture(stream_url)

# if not video_capture.isOpened():
#     print("Error: Unable to open video stream")
# else:
#     print("Stream opened successfully")
#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             print("Error: Unable to read frame")
#             break
#         cv2.imshow('Video', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()


import requests

stream_url = "http://niruta:niruta@192.168.72.32:8080/video"
response = requests.get(stream_url, stream=True)

if response.status_code == 200:
    print("Stream is accessible")
else:
    print(f"Failed to access stream, status code: {response.status_code}")
