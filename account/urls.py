from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.login, name='signin'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signinfacebook/', views.signinfacebook, name='signinfacebook'),
    path('signingoogle/', views.signingoogle, name='signingoogle'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/editprofile/<int:user_id>/', views.editprofile, name='editprofile'),
]
