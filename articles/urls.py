from django.urls import path
from .views import ArticleListView, DetailArticleView, DeleteArticleView, UpdateArticleView,CreateArticleView,CommentCreateView
urlpatterns = [
    path('<int:pk>/edit/', UpdateArticleView.as_view(), name='article_edit'), 
    path('<int:pk>/',DetailArticleView.as_view(), name='article_detail'),  
    path('<int:pk>/delete/',DeleteArticleView.as_view(), name='article_delete'),
    path('<int:pk>/comment/',CommentCreateView.as_view(), name='article_comment'),
    path('new/',CreateArticleView.as_view() , name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),

]
