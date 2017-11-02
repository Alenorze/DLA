from django.conf.urls import url
from django.contrib import admin

from pages.views import HomeView, PageDetailView
from newsletter.api.views import JoinCreateAPIView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/$', PageDetailView.as_view(), name='page-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/email/join/$',JoinCreateAPIView.as_view(), name='email-join'),
]
