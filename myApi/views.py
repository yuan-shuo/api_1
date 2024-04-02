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
    
def getWord(request):
    if request.method == 'GET':
        # 获取所有 textDic 对象的 title、date 和 message_content 属性
        data = textDic.objects.select_related().values('title', 'date', 'message_content')

        # 将结果转换为列表
        data_list = list(data)

        print("Data List:", data_list)
        # return HttpResponse("Ok!")
        return JsonResponse(data_list, safe=False)
    return HttpResponse("not GET")
        