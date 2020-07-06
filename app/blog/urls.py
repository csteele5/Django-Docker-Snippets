from django.urls import path

from blog.views import (article_detail_view,
                            article_create_view, 
                            article_update_view, 
                            article_delete_view, 
                            article_list_view)
app_name = 'articles'
urlpatterns = [
    path('create/', article_create_view, name='article-create'),
    path('', article_list_view, name='article-list'),
    path('<int:id>/update/', article_update_view, name='article-update'),
    path('<int:id>/delete/', article_delete_view, name='article-delete'),
    path('<int:id>/', article_detail_view, name='article-detail'),
]
