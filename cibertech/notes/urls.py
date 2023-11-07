

from django.urls import path
from . import views
urlpatterns = [
    path('noteBooks/', views.noteBookListView.as_view()),
    path('notePages/', views.notesPagesListView.as_view()),
    path('noteBook/<int:BookId>/notePages', views.noteBookPagesView.as_view()),
    path('noteBooks/<int:noteBookId>/', views.noteBookDetailView.as_view()),
    path('notePages/<int:notePageId>/', views.notePagesDetailView.as_view()),
  
]