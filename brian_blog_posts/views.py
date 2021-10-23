from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import TopicForm

def index(request):
	"""The home page for Brian's blog posts."""
	return render(request, 'brian_blog_posts/index.html')

def blog_posts(request):
	"""Show all blog posts."""
	blog_posts = BlogPost.objects.order_by('date_added')
	context = {'blog_posts': blog_posts}
	return render(request, 'brian_blog_posts/blog_posts.html', context)

def blog_post(request, blog_post_id):
	"""Show a post."""
	blog_post = BlogPost.objects.get(id=blog_post_id)
	context = {'blog_post': blog_post}
	return render(request, 'brian_blog_posts/blog_post.html', context)

@login_required
def new_blog_post(request):
	"""Add a new blog post."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data.
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_blog_post = form.save(commit=False)
			new_blog_post.owner = request.user
			new_blog_post.save()
			return redirect('brian_blog_posts:blog_posts')

	#Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'brian_blog_posts/new_blog_post.html', context)

@login_required
def edit_blog_post(request, blog_post_id):
	"""Edit an existing blog post."""
	blog_post = BlogPost.objects.get(id=blog_post_id)
	#Make sure the post belongs to the current user!
	if blog_post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request; pre-fill form with the current entry.
		form = TopicForm(instance=blog_post)
	else:
		# POST data submitted; process data.
		form = TopicForm(instance=blog_post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('brian_blog_posts:blog_post', blog_post_id=blog_post.id)

	context = {'blog_post': blog_post, 'form': form}
	return render(request, 'brian_blog_posts/edit_blog_post.html', context)















