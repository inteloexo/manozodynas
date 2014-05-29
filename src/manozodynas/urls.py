from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view, login_view, words_view, NewWord

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^login$', login_view, name='login'),
    url(r'^words/$', words_view, name='words'),
    url(r'^new/$', NewWord.as_view(), name='new_word'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
