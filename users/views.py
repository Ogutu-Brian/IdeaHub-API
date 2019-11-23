from django.http import HttpResponse,request

def index(request):
    return HttpResponse('Hello there welcome to idea hub')
    