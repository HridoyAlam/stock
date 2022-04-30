from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('about.html', views.about, name="about"),
    path('test.html', views.test, name='test'),
    path('d_page1.html', views.page1, name='page1'),
    path('d_page2.html', views.page2, name='page2'),
    path('name.html', views.get_name, name='name'),
    path('profile.html', views.profile, name='profile'),
    
]