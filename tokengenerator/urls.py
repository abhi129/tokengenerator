from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from tokengenerator import views



urlpatterns = [
url(r'^home/$', views.home,name="home"),
url(r'^generate/$', views.tokengenerator,name="tokengenrator"),
url(r'^alltokens/$', views.seeall,name="seeall"),
url(r'^delete/$', views.delete,name="delete"),
url(r'^assigntoken/$', views.assign,name="assign"),
url(r'^unblock/$', views.unblock,name="unblock"),
url(r'^claim/$', views.claim,name="claim"),
url(r'^remove/$', views.remove,name="remove"),
url(r'^alive/$', views.alive,name="alive"),
# url(r'^aboutus/$', views.aboutus,name="aboutus"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)