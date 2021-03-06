from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProjectViewSet, ProjectCreateView


router = SimpleRouter()
router.register('users', UserViewSet, )
router.register('', ProjectViewSet,)

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name='newproject'),
    # path("post/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
]

urlpatterns += router.urls