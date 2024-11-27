from django.urls import path
from .views import login_page, register_page, logout_page,home,about

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_page, name='logout_page'),
     path('home/', home, name='home'),
      path('about/', about, name='about'),
]



