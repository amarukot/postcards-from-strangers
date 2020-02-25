from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.postcard_list, name='postcard_list'),
    path('postcards/', views.postcard_list, name='postcard_list'),
    path('postcard/<int:pk>/', views.postcard_detail, name='postcard_detail'),
    # path('favorites/postcard/<int:pk>/', views.postcard_detail, name='postcard_detail'),
    path('postcard/create', views.postcard_create, name='postcard_create'),
    path('postcard/edit/<int:pk>', views.postcard_edit, name='postcard_edit'),
    path('postcard/delete/<int:pk>', views.postcard_delete, name='postcard_delete'),
    path('postcard/favorite/<int:pk>', views.postcard_favorite, name='postcard_favorite'),
    path('favorites/', views.favorites, name='favorites'),

# to display the images from static/ media folder
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

