from django.urls import path
from .views import (
	CourseListView,
	CourseDetailView,
	CourseCreateView,
	CourseUpdateView,
	CourseDeleteView
	)
#IMPORTANT: This is a class based view approach, vs a function bases view approach.  
#The class based view requires a specific location/naming convention for the template
# i.e. When looking at a list: appname/modelname_viewname.html  articlesnew/article_list.html
#VERY IMPORTANT!
app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    path('<int:id>/', CourseDetailView.as_view(), name='courses-detail'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
] 