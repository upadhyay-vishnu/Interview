from django.conf.urls import patterns, include, url
from .views import insert_url, Url_Detail_Update, Tag_Detail_Upadte, Create_Tag, Edit_URL, Edit_Tag

urlpatterns = patterns('',
    url(r'^bookmark/$', insert_url.as_view(), name='inserturl'),
    #url(r'^bookmark/(?P<pk>[0-9]+)/$', UrlList.as_view(), name='UrlList'),
  #  url(r'^deleteurl/$', Delete_Tag.as_view(), name='deleteurl'),
    url(r'^bookmarks/(?P<pk>[0-9]+)/$', Url_Detail_Update.as_view(), name='showurl'),
    url(r'^bookmarks/(?P<pk>[0-9]+)/edit/$', Edit_URL.as_view(), name='editurl'),
    url(r'^tags/(?P<pk>[0-9]+)/edit/$', Edit_Tag.as_view(), name='edittag'),
    url(r'^tags/(?P<pk>[0-9]+)/$', Tag_Detail_Upadte.as_view()),
    url(r'^tags/new/$', Create_Tag.as_view()),

)