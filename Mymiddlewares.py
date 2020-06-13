from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
class Md1(MiddlewareMixin):
    def process_request(self,request):
        print("Md1请求")
        # print(request)
        # print(request.method)
        # print(request.session.clear())
        # print(request.session.keys())
        # print(request.path)
        # if 'root' not in request.session or not request.session['root']:
        #     print('url过滤')
    def process_response(self,request,response):
        print("Md1返回")
        return response


class Md2(MiddlewareMixin):
    def process_request(self,request):
        print("Md2请求")
    def process_response(self,request,response):
        print("Md2返回")
        return response