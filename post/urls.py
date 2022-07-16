from django.urls import path, include
from .views.post_list import post_list
from .views.post_detail import post_detail

urlpatterns = [
    path('', post_list, name='post_lists_page'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', post_list, name='post_lists_page_bt_tag'),

]