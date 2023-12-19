from django.urls import path

from . import views

urlpatterns = [
    path('ques', views.all_questions, name='question'),
    path('add', views.CreateQuestion.as_view(), name='add'),
    path('ques/<int:pk>', views.DetailQuestion.as_view(), name='detail'),
    path('ques/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('search/', views.search, name='search'),
    path('like/<int:pk>/', views.LikeView, name='like'),
]
