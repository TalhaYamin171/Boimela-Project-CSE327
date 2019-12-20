from django.urls import path, include
from . import views
from .views import StallListView, StallDetailView, StallCreateView, StallUpdateView, StallDeleteView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', views.home, name='boimelawebApp-home'),
    path('latest/', views.latest, name='boimelawebApp-latest'),
    path('dashboard/', StallListView.as_view(), name='dashboard'),
    path('stall/<int:pk>/', StallDetailView.as_view(), name='stall-detail'),
    path('stall/new/', StallCreateView.as_view(), name='stall-create'),
    path('stall/<int:pk>/update/', StallUpdateView.as_view(), name='stall-update'),
    path('stall/<int:pk>/delete/', StallDeleteView.as_view(), name='stall-delete'),
    path('navigation/', views.navigation, name='boimelawebApp-navigation'),
    path('search/', views.searchposts, name='boimelawebApp-search'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
