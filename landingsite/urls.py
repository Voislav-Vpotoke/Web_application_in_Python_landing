from django.contrib import admin
from django.urls import path
from crm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('thanks/', views.thanks_page, name = 'thanks_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
