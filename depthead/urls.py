from django.urls import path
from .import views
urlpatterns = [
    
    path('login/',views.login),
    path('login/authentication',views.login_view),
]