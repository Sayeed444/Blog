from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view() ,name = 'home' ),
    path('details/<int:pk>/', views.PostDetailView.as_view() ,name = 'detail' ),
    path('New/post/', views.PostCreateView.as_view() ,name = 'new_post' ),
]
