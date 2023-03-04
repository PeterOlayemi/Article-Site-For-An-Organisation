from django.urls import path
from . import views

app_name='foods'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register.as_view(), name='register'),
    path('editcomment/<int:id>/', views.editcomment, name='editcomment'),
    path('addcomment/', views.addcomment, name='addcomment'),
    path('delete/<int:id>/', views.deletecomment, name='deletecomment'),
    path('viewyourcomment/', views.viewyourcomment, name='viewyourcomment'),
]
