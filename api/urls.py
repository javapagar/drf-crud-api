from rest_framework import routers
from .endpoints import ToDoViewSet

router = routers.DefaultRouter()

router.register("api/v1/to-do", ToDoViewSet,'to-do')

urlpatterns = router.urls