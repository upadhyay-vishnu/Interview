from django.conf.urls import patterns, include, url
from .views import insert_url, UrlList, GetUrl, Delete_Tag, Url_Detail_Update, Tag_Detail_Upadte, Create_Tag

urlpatterns = patterns('',
    url(r'^bookmark/$', insert_url.as_view(), name='inserturl'),
    #url(r'^bookmark/(?P<pk>[0-9]+)/$', UrlList.as_view(), name='UrlList'),
    url(r'^geturl/$', GetUrl.as_view(), name='GetUrl'),
    url(r'^deleteurl/$', Delete_Tag.as_view(), name='deleteurl'),
    url(r'^bookmarks/(?P<pk>[0-9]+)/$', Url_Detail_Update.as_view(), name='urldetail'),
    url(r'^tags/(?P<pk>[0-9]+)/$', Tag_Detail_Upadte.as_view()),
    url(r'^tags/new/$', Create_Tag.as_view()),

)