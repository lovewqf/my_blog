from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
import pdb
# Create your views here.
def show_index(request):
    return render(request,'index.html')


@csrf_exempt
def show_request(request):
    results = Catagory.objects.all()
    blog_results = Blog.objects.all()
    print(results)
    cagatory_list,blog_list = [],[]
    for result in results:
        cagatory_list.append(result.catagory_name)
    for blog_obj in blog_results:
        blog_list.append(blog_obj.content)
    print(cagatory_list)
    print(blog_list)
    msg = {'code':200,'infor':cagatory_list,'content':blog_list}
    return HttpResponse(json.dumps(msg))

@csrf_exempt
def show_cagatory_blog(request):
    pass
