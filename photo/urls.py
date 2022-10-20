from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    path('img_info/<int:id>/', views.img_info, name='img_info'),
    path('img_info/<int:id>/delete', views.img_info, name='delete'),
    path('img_info/<int:id>/favorit', views.favorit, name='favorit'),
    path('trash/', views.trash, name='trash'),
    path('favorit/', views.favorit_view, name='favorit_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
