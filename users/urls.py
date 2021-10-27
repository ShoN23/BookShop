from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SignUpPageView

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name='signup'),
    
]