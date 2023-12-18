from django.urls import path

from .views import Login, Logout, UserProfile,signup

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', UserProfile.as_view(), name='profile'),
    path('signup', signup, name='signup'),
]
