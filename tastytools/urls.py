import os
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from views import doc, howto
from django.views.static import serve

def my_serve(request, path, document_root=None, show_indexes=False, *args, **kwargs):
    path =  "static/" + path
    document_root = os.path.dirname(os.path.abspath(__file__))
    return serve(request, path, document_root, show_indexes)

urlpatterns = patterns('',
    (r'^doc', doc),
    (r'^howto', howto),
    url(r'^static/(?P<path>.*)$', my_serve, name='tastytools_static_url')
)
