"""Defines URL patterns for brian_blog_posts."""

from django.urls import path

from . import views

app_name = 'brian_blog_posts'
urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	#Page that views all blog posts
	path('blog_posts/', views.blog_posts, name='blog_posts'),
	#Page to view a single blog post
	path('blog_posts/<int:blog_post_id>/', views.blog_post, name='blog_post'),
	#Page for adding a new blog post
	path('new_blog_post/', views.new_blog_post, name='new_blog_post'),
	#Page for editing entries
	path('edit_blog_post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
]
