from topics.views import TopicViewSet, PostIdViewSet, SubscriberViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('topics', TopicViewSet)
router.register('post_ids', PostIdViewSet)
router.register('subscribers', SubscriberViewSet)
router.register(r'topics/(?P<topic>[^/.]+)/post_ids', PostIdViewSet)
router.register(r'topics/(?P<topic>[^/.]+)/subscribers', SubscriberViewSet)
