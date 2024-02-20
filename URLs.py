from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ParagraphViewSet, WordViewSet, WordSearchView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'paragraphs', ParagraphViewSet)
router.register(r'words', WordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('word-search/<str:word>/', WordSearchView.as_view()),
]
