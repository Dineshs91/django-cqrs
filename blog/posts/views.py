from django.views import View
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


class PostView(View):
    def get(self, request):
        context = RequestContext(request)
        context_dict = {}
        return render_to_response('posts.html', context_dict, context)

    def post(self, request):
        return HttpResponse('hi')
