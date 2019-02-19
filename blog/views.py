from django.shortcuts import render
from pprint import pprint

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})