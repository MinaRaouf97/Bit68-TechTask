
from django.urls import path, re_path
from .views import RegisterView,LoginView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    
    

]