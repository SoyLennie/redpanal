from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from views import AudioCreateView, AudioDetailView, AudioUpdateView, AudioDeleteView


urlpatterns = patterns('redpanal.audio.views',
    url(r'^upload/$', AudioCreateView.as_view(), name='audio-create'),
    #url(r'^list/$', "list", name='audio-list',
    url(r'^(?P<slug>[\w-]+)/$', AudioDetailView.as_view(), name='audio-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', AudioUpdateView.as_view(), name='audio-edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', AudioDeleteView.as_view(), name='audio-delete'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
