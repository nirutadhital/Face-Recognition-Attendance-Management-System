from django.shortcuts import render
import keras
from rest_framework import generics, mixins
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from rest_framework.views import APIView
import numpy as np
from PIL import Image
import cv2
import base64
import os
import tensorflow as tf
import cv2
from mtcnn import MTCNN

class UserSignup(APIView):
    def __init__(self):
        try:
            model_path = os.path.join(os.path.dirname(__file__), 'facenet_keras_trained.keras')
            self.facenet_model = tf.keras.models.load_model(model_path)
        except Exception as e:
            print(f"Error loading FaceNet model: {e}")
            raise

    def preprocess_image(self, image):
        # Resize to 160x160 and normalize pixel values
        image = cv2.resize(image, (160, 160))
        image = (image.astype('float32') - 127.5) / 128.0
        return np.expand_dims(image, axis=0)

    def extract_face_embedding(self, image):
        # Preprocess the image and generate the embedding
        image = self.preprocess_image(image)
        embedding = self.facenet_model.predict(image)
        return embedding.flatten()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        image_file = request.FILES.get("common/photo")
        if not image_file:
            return Response({"error": "Image file is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Load and convert the image
            image = Image.open(image_file)
            image = image.convert("RGB")
            image_array = np.array(image)

            # Extract face embedding using FaceNet
            face_embeddings = self.extract_face_embedding(image_array)

            # Convert embedding to a string for storage
            face_embedding_str = base64.b64encode(face_embeddings).decode("utf-8")
            added_by_id=1
            company_id=1
            department_id=1
            faculty_id=1
            grades_id=1

            # Save the user and embedding
            serializer.save(face_embeddings=face_embedding_str, added_by_id=added_by_id, company_id=company_id, department_id=department_id, faculty_id=faculty_id,grades_id=grades_id)
            return Response({"message": "User signed up successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"Error processing the image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

user_signup_view=UserSignup.as_view()



# class FaceRecognitionView(APIView):
#     def __init__(self):
#         # Load FaceNet model
#         try:
#             model_path = os.path.join(os.path.dirname(__file__), 'facenet_keras_trained.keras')
#             self.facenet_model = tf.keras.models.load_model(model_path)
#         except Exception as e:
#             print(f"Error loading FaceNet model: {e}")
#             raise

#         # Initialize MTCNN for face detection
#         self.detector = MTCNN()

#     def preprocess_image(self, image):
#         # Resize to 160x160 and normalize pixel values
#         image = cv2.resize(image, (160, 160))
#         image = (image.astype('float32') - 127.5) / 128.0
#         return np.expand_dims(image, axis=0)

#     def extract_face_embedding(self, image):
#         # Preprocess the image and generate the embedding
#         image = self.preprocess_image(image)
#         embedding = self.facenet_model.predict(image)
#         return embedding.flatten()

#     def compare_embeddings(self, embedding1, embedding2):
#         # Calculate cosine similarity
#         dot_product = np.dot(embedding1, embedding2)
#         norm1 = np.linalg.norm(embedding1)
#         norm2 = np.linalg.norm(embedding2)
#         similarity = dot_product / (norm1 * norm2)
#         return similarity

#     def get(self, request):
#         # RTSP or HTTP URL for the mobile camera stream
#         # stream_url = request.query_params.get('http://niruta:niruta@192.168.72.32:8080/video')
#         stream_url='http://niruta:niruta@192.168.72.32:8080/video'
#         if not stream_url:
#             return Response({"error": "Stream URL is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Open the video stream
#         video_capture = cv2.VideoCapture(stream_url)
#         if not video_capture.isOpened():
#             return Response({"error": "Unable to open video stream"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         def generate_frames():
#             while True:
#                 ret, frame = video_capture.read()
#                 if not ret:
#                     break

#                 # Detect faces using MTCNN
#                 faces = self.detector.detect_faces(frame)
#                 print(f"Number of faces detected: {len(faces)}")
                
#                 if len(faces) == 0:
#                     # Encode the frame as JPEG even if no faces are detected
#                     ret, buffer = cv2.imencode('.jpg', frame)
#                     frame = buffer.tobytes()
#                     yield (b'--frame\r\n'
#                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#                     continue
                
                
#                 for face in faces:
#                     x, y, width, height = face['box']
#                     face_image = frame[y:y+height, x:x+width]

#                     # Extract face embedding
#                     try:
#                         face_embedding = self.extract_face_embedding(face_image)
#                         print("Generated Live user Embedding",face_embedding)#Generated Live user Embedding [0.5664406]
#                     except Exception as e:
#                         continue

#                     # Compare with embeddings in the database
#                     closest_match = None
#                     max_similarity = 0.6 #-1
#                     for user in User.objects.all():
#                         print("This is face embedding from db",user.face_embeddings)#This is face embedding from db sGMUPw==
                        
#                         # db_embedding = np.frombuffer(base64.b64decode(user.face_embeddings), dtype=np.float32)#Error is in this line?
#                         # print("this is testing",db_embedding)
#                         try:
#                             # Decode the base64-encoded embedding
#                             embedding_bytes = base64.b64decode(user.face_embeddings)
#                             db_embedding = np.frombuffer(embedding_bytes, dtype=np.float32)
#                             print("Decoded DB Embedding", db_embedding)
#                             similarity = self.compare_embeddings(face_embedding, db_embedding)
#                             print(f"Similarity with user {user.id}: {similarity}")
#                             if similarity > max_similarity:
#                                 max_similarity = similarity
#                                 closest_match = user
#                         except Exception as e:
#                             print(f"Error decoding face_embeddings for the user {user.id}:{e}")
#                             continue

#                     # Display "Present" or "Not Present"
#                     if closest_match and max_similarity > 0.6:  
#                         status_text = "Present"
#                         print(f"Present for {user.id}")
#                         box_color = (0, 255, 0)  # Green color for "Present"
#                     else:
#                         status_text = "Not Present"
#                         box_color = (0, 0, 255)  # Red color for "Not Present"

#                     # Draw bounding box and status text
#                     cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)
#                     cv2.putText(frame, status_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

#                 # Encode frame as JPEG
#                 ret, buffer = cv2.imencode('.jpg', frame)
#                 frame = buffer.tobytes()
#                 yield (b'--frame\r\n'
#                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#         # Return the video stream as a response
#         return Response(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

# face_recognition_view = FaceRecognitionView.as_view()





# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# user_list_create_view=UserListCreateAPIView.as_view()

# class UserUpdateAPIView(generics.UpdateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# user_update_view=UserUpdateAPIView.as_view()


# class UserDestroyAPIView(generics.DestroyAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# user_destroy_view=UserDestroyAPIView.as_view()
    
    
    
