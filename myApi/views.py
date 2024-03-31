from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myApi.models import textDic

# Create your views here.
def index(request):
    return HttpResponse("hello world!")

def dataBack(request):
    data = {
        'meta': {
            'status': 200
        },
        'message': "this is a mes from yuan.s api"
    }
    return JsonResponse(data)

def leaveWord(request):
    data = {
        "title": "调试用标题",
        "message_content": "调试用内容",
        "author_name": "调试用名字"
    }
    textDic.objects.create(title=data["title"],
                           message_content=data["message_content"],
                           author_name=data["author_name"])
    return HttpResponse("Ok!")