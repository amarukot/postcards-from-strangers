from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.postcard_list, name='postcard_list'),
    path('postcards/', views.postcard_list, name='postcard_list'),
    path('postcard/<int:pk>/', views.postcard_detail, name='postcard_detail'),
    # path('postcard/create', views.postcard_create, name='postcard_create'),
    # path('postcard/edit/<int:id>', views.postcard_edit, name='postcard_edit'),
    # path('postcard/delete/<int:id>', views.postcard_delete, name='postcard_delete'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# To display the images from static/ media folder
