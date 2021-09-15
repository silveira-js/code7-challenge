from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', views.AuthorView)
router.register('news', views.NewsView)

urlpatterns = [
    path('v1/', include(router.urls)),
]
