
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from . import settings

# from prateekstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , include('prateekstore.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
