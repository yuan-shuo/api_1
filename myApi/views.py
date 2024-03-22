from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world!")

def dataBack(request):
    data = {"name":"yuan","age":21}
    return JsonResponse(data, safe=False)