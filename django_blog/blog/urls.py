from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post URLs
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('post/comments/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('post/comments/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
]
