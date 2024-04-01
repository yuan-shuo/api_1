from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myApi.models import textDic
import json

from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def leaveWord(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        textDic.objects.create(title=data["title"],
                           message_content=data["content"],
                           author_name=data["name"])
        return HttpResponse("Ok!")
        # print(data['title'])
        
        # title = request.POST.get('title', '')  # 获取标题
        # content = request.POST.get('content', '')  # 获取留言内容
        # name = request.POST.get('name', '')  # 获取留言人的名字
        
        # data = {
        #     "title": "调试用标题",
        #     "message_content": "调试用内容",
        #     "author_name": "调试用名字"
        # }
        # textDic.objects.create(title=data["title"],
        #                        message_content=data["message_content"],
        #                        author_name=data["author_name"])
        