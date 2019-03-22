from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'url_texts', views.UrlTextViewSet, base_name="url_texts")


urlpatterns = [
    path('', include(router.urls)),
]
