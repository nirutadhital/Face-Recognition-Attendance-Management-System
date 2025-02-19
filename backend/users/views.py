from django.shortcuts import render
import keras
from rest_framework import generics, mixins
from users.models import User, Token
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
from django.contrib.auth import authenticate

class UserSignup(APIView):
    def __init__(self):
        try:
            model_path = os.path.join(os.path.dirname(__file__), '../common/facenet_keras_trained.keras')
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

        image_file = request.FILES.get("photo")
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
            company_id = request.data.get('company_id', 1)
            department_id = request.data.get('department_id', 1)
            faculty_id = request.data.get('faculty_id', 1)
            grades_id = request.data.get('grades_id', 1)
            
            print("this is company",company_id)
            print("this is department",department_id)
            print("this is faculty",faculty_id)
            print("this is grade",grades_id)
            # Save the user and embedding
            user=serializer.save(face_embeddings=face_embedding_str,  department_id=department_id, faculty_id=faculty_id,grades_id=grades_id,company_id=company_id)
            token=Token.objects.create(user=user)
         
            print("This is TOken",token)
            
            return Response({"message": "User signed up successfully", "token":token.key, "password":user.password}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"Error processing the image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

user_signup_view=UserSignup.as_view()




class UserLogin(APIView):
    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")
        print(f"Username:{username}, Password:{password}")
        
        try:
            user = User.objects.get(username=username)
            print(f"User found: {user.username}")  # Debugging
        except User.DoesNotExist:
            print("User does not exist")  # Debugging
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        print(f"User Outside {username}")
        
         # Check if the user is active
        if not user.is_active:
            print("User is not active")  # Debugging
            return Response(
                {"error": "User is not active"}, status=status.HTTP_401_UNAUTHORIZED
            )
            
        user=authenticate(username=username, password=password)

        if not user:
            print(f"this is debugging{user}")
            print(f"Authentication Failed")
            return Response(
                {"error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
            
        print(f"Authenticated User:  {user.username}")

        Token.objects.filter(user=user).delete()
        
        token=Token.objects.create(user=user)
        return Response(
            {
                "message":"Login Successful!",
                "token":token.key
            },
            status=status.HTTP_200_OK
        )
        

user_login_view=UserLogin.as_view()
        






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
    
    
    
