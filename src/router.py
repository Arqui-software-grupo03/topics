from topics.views import TopicViewSet, PostViewSet, SubscriberViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
router.register(r'topics/(?P<topic>[^/.]+)/posts', PostViewSet)
router.register(r'topics/(?P<topic>[^/.]+)/subscribers', SubscriberViewSet)
