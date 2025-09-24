from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializers, AuthorSerializer
from .models import Author


#Authentication import 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def Register(request):
    serializer = UserSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': "Register successful"}, status=status.HTTP_200_OK)
    else: 
        return Response({"message": serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)




@extend_schema(
        summary="To login the user",
        request=dict,
        examples= [
            OpenApiExample(
                name= "Login User",
                value={
                    "first_name": "first name here",
                    "last_name": "last name here",
                    "email": "value here",
                    "password":"password",
                    "role": "role here"

                }
            )
        ]
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def Login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email= email, password= password)
    

    if user is not None: 
       access = AccessToken.for_user(user)
       refresh = RefreshToken.for_user(user)
       return Response({'message': "Login is  successful", "access": str(access), "refresh": str(refresh)}, status=status.HTTP_200_OK)
    else: 
        return Response({"message": "Your username or password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def create_news(request):
    if Author.objects.filter(user=request.user).exists():
        return Response({"message": "An author data hs already been created with this user"}, status=status.HTTP_404_NOT_FOUND)
    
    author_data = request.data
    serializer = AuthorSerializer(data=author_data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "Author created successful", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
      return Response({"message": "Something went wrong","error": serializer.data}, status=status.HTTP_401_UNAUTHORIZED)

