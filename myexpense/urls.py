from rest_framework import routers
from .api import MyExpenseViewSet

# urlpatterns = [
#     path('',MyExpenseViewSet,'myexpense')
# ]

router = routers.DefaultRouter()
router.register('',MyExpenseViewSet, 'myexpense')

urlpatterns = router.urls