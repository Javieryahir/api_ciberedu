

from django.urls import path
from . import views
urlpatterns = [
    path('noteBooks/', views.noteBookListView.as_view()),
    path('noteBook/', views.noteBookCreateView.as_view()),
    path('noteBookD/<int:noteBookId>/', views.noteBookDetailView.as_view())

  
]