from rest_framework import routers
from article.viewsets import ArticleVieweSet

router = routers.DefaultRouter()
router.register(r'article', ArticleVieweSet)