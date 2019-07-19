from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('new/', views.new, name='new'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 