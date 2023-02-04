from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.SimpleRouter()
router.register('users', views.UserViewSet)
router.register('notes', views.NoteViewSet)
router.register('drawings', views.DrawingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
