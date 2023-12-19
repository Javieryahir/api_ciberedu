from django.urls import path
from . import views
urlpatterns = [
    path('categories/', views.categoryListView.as_view()),
    path('message/', views.messageListView.as_view()),
    path('messages/<int:CategoryId>/', views.messagesbyCategoryListView.as_view())
  
]