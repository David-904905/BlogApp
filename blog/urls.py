from django.urls import path
from . views import home, post_detail,  post_edit, post_delete

urlpatterns = [
    path('', home, name='homepage'),
    path('post-detail/<int:pk>/', post_detail, name='post-detail-link'),
    path('post-edit/<int:pk>/', post_edit, name='blog-post-edit'),
    path('post-delete/<int:pk>/', post_delete, name='blog-post-delete'),

]