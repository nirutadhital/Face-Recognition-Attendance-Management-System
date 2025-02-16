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
    
    
    
