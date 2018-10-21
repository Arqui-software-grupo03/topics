from topics.views import TopicViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
