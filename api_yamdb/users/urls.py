from api.views import signup_user, token_user
from django.urls import path

urlpatterns = [
    path('signup/', signup_user),
    path('token/', token_user),
]
