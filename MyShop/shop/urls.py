from django.urls import path, include
from .views import hellowold

urlpatterns = [
    path('', hellowold)
]