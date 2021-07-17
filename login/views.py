from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework import status 
from rest_framework import permissions, authentication 
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserInfoSerializer, ChangePasswordSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# from django.contrib.auth.models import User

class SignupView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        #retrieves the form data
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        # password2 = data['password2'] 
        if password:
            if User.object.filter(email=email).exists():
                return Response({'error':'Email already exists'})
            else:
                if len(password) < 6: 
                    return Response({'error':'Password must be atleast 6 character'})
                else:
                    user = User.object.create_user(email = email, password = password, name = name)
                    user.save()
                return Response({'success':'User created successfully'})

        else: 
            return Response({'error':'Passwords do not match'})


class ListUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, format = None):
        email = [User.email for user in User.objects.all()]
        return Response(email)

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
          
        })
    
class UpdatePassword(generics.UpdateAPIView):
    model = User 
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangePasswordSerializer  
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
# @api_view(['GET'])
# def profile(request):
class Profile(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        user = request.user
        serialized_user = UserInfoSerializer(user).data
        print(serialized_user)
        return Response({'user': serialized_user })

