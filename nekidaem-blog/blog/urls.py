from django.urls import path

from .views import (
    BlogListView, BlogDetailView, PostListView, PostDetailView,
    BlogSubscribeView, BlogUnsubscribeView, PostCreateView, PostDeleteView,
    PostMarkAsReadView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('posts', PostListView.as_view(), name='post_list'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(),
         name='post_delete'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/mark_as_read',
         PostMarkAsReadView.as_view(), name='post_mark_as_read'),
    path('<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/subscribe', BlogSubscribeView.as_view(), name='subscribe'),
    path('<int:pk>/unsubscribe', BlogUnsubscribeView.as_view(),
         name='unsubscribe')
]
