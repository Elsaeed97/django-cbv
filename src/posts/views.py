from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class HomePage(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.all()
		return context

class PostsDetail(DeleteView):
	context_object_name = 'post_details'
	model = Post
	template_name = 'posts/post_detail.html'

class PostCreate(CreateView):
	fields = ('title', 'content','author')
	model = Post

class PostUpdate(UpdateView):
	fields = ('title', 'content')
	model = Post 

class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('home')

