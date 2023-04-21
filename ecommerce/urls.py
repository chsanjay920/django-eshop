
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from . import settings

# from prateekstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , include('prateekstore.urls'))
    # path('', views.kamal),
    # path('kamal', views.kamal),
    # path('index/',views.kamal),
    # path('home/',views.home),
    # path('contact/',views.contact),
    # path('product/',views.product),
    # path('account/',views.account),
    # path('about/',views.about),
    # path('cart/',views.cart),
    # path('AdjustableWrench/', views.AdjustableWrench),
    # path('DrillingMachine/',views.DrillingMachine),
    # path('GumBoots/',views.GumBoots),
    # path('Hammer/',views.Hammer),
    # path('Helmet/',views.Helmet),
    # path('Pliers/',views.Pliers),
    # path('SafetyGlasses/',views.SafetyGlasses),
    # path('ScrewdriverMachine/',views.ScrewdriverMachine),
    # path('SpannerSet/',views.SpannerSet),
    # path('WeldingGloves/',views.WeldingGloves),
    # path('WeldingHolder/',views.WeldingHolder),
    # path('WeldingMachine/',views.WeldingMachine),
    # path('home/',views.signin, name='signin')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
