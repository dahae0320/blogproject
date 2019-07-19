from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new1/', views.new1, name='new1'),
    path('update1/<int:pk>', views.update1, name='update1'),
    path('delete1/<int:pk>', views.delete1, name='delete1'),
]