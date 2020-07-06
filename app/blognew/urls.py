from django.urls import path
from .views import (
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView
	)
#IMPORTANT: This is a class based view approach, vs a function bases view approach.  
#The class based view requires a specific location/naming convention for the template
# i.e. When looking at a list: appname/modelname_viewname.html  articlesnew/article_list.html
#VERY IMPORTANT!
app_name = 'articlesnew'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articlesnew-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='articlesnew-detail'),
    #path('<int:pk>/', ArticleDetailView.as_view(), name='articlesnew-detail'),
    #path('(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='articlesnew-detail'),
    #path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='articlenew-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]