from django.views import View
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

from posts.models import Post
from posts.forms import PostForm


class PostView(View):
    def get(self, request):
        context_dict = {}

        posts = Post.objects.all().order_by('created_at')
        context_dict['posts'] = posts

        post_form = PostForm()
        context_dict['post_form'] = post_form

        return render(request, 'posts.html', context_dict)

    def post(self, request):
        context_dict = {}

        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()

        posts = Post.objects.all().order_by('created_at')
        context_dict['posts'] = posts

        post_form = PostForm()
        context_dict['post_form'] = post_form
        return render(request, 'posts.html', context_dict)
