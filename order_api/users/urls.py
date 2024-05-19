from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
