from topics.views import TopicViewSet, PostIdViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
router.register(r'topics/(?P<topic>[^/.]+)/post_ids', PostIdViewSet)
