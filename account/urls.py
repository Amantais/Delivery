from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RegisterView, ActivationView,  ProfileViewSet, LogoutAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('profile/', ProfileViewSet.as_view({'get': 'retrieve',
                                            'patch': 'partial_update',
                                            'put': 'update'}))
]  

