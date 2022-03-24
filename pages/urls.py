from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('<str:username>/addwork', views.addwork, name='addwork'),
    path('account/profile/photo/<int:id>/', views.photodetails, name='photodetails'),
    path('account/profile/photo/<int:id>/editwork/', views.editwork, name='editwork'),
    path('blog', views.blog, name='blog'),
    path('blog/blogdetails/<int:id>/', views.blogdetails, name='blogdetails'),
    path('blog/blogdetails/<int:id>/savecommentnotregister', views.savecommentnotregister, name='savecommentnotregister'),
    path('blog/blogdetails/<int:id>/savecommentregister', views.savecommentregister, name='savecommentregister'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('contacthomepage/', views.contacthomepage, name='contacthomepage'),
    path('account/profile/photo/<int:id>/delete/', views.photodelete, name='photodelete'),
]
