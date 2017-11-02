from django.conf.urls import url
from django.contrib import admin

from newsletter.api.views import JoinCreateAPIView
from pages.views import HomeView, PageDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/email/join/$', JoinCreateAPIView.as_view(), name='email-join'),
    url(r'^(?P<slug>[\w-]+)/$', PageDetailView.as_view(), name='page-detail'),

]