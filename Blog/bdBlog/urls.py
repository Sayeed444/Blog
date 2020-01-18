from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(),name ='home'),
    path('user/<str:username>',views.UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name = 'detail'),
    path('New/post/', views.PostCreateView.as_view(),name ='new_post'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
