from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from m33_messaging.users.api.views import (RegistrationView,
                                         
                                           )

app_name = "users"
urlpatterns = [
    path('auth/register/', RegistrationView.as_view(), name='register'),

    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Use TokenObtainPairView for login
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh view
]