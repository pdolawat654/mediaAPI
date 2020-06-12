from django.urls import path
from . import views
urlpatterns=[
    path('',views.posts,name='posts'),
    path('id/<str:pk>',views.get_post_by_id,name='get_post_by_id'),
    path('delete/<str:pk>',views.delete_post,name='delete_post'),
    path('add',views.add_post,name='add_post'),
    path('user/<str:artist_id>',views.get_posts_for_user,name='get_posts_for_user'),
    path('update/<str:pk>',views.update_post,name='update_post'),
]