from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomJWTSerializer
from . import views


urlpatterns = [
    path('login', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='login'),
    path('register', include('rest_auth.registration.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
