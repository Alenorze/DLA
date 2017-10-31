from django.conf.urls import url
from django.contrib import admin

from pages.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='homec'),
    url(r'^admin/', admin.site.urls),
    
]
