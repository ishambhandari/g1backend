from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token 
from .views import SignupView, ListUser, Profile, CustomAuthToken, UpdatePassword
urlpatterns = [
    path('api/users/', ListUser.as_view()),
    path('signup/', SignupView.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('getcurrentuser/', Profile.as_view(), name = "getUser"),
    path('changepassword/',UpdatePassword.as_view(), name = 'changepassword'),

]
