from django.urls import path, include
from portal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('deportistas/', views.deportista_list),
    path('deportista/<int:pk>', views.deportista_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
