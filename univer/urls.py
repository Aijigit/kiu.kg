from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
   	# path('login/', views.user_login, name='login'),
   	# path('register/', views.register, name = 'register')
]