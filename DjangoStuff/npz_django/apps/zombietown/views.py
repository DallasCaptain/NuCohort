from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    response = 'super'
    response += 'cali'
    response +='nope'

    return HttpResponse(response)

def bob(request):


    return HttpResponse('Carl was here')

def money(request):
    return HttpResponse('$0')
