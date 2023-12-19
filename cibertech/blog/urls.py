from django.urls import path
from . import views
urlpatterns = [
    path('post/', views.BlogListView.as_view()),
    path('postCovers/', views.frontBlogListView.as_view()),
    path('postContent/<int:BlogId>/', views.contentBlogListView.as_view()),
]