from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]