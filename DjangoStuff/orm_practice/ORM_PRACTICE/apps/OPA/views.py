from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    u = User.objects.first()
    context = {
        'user':u,
    }
    print (u)

    return render(request,'OPA/index.html',context)


def proc(request):
    print (request.POST)
    print('*'*20)
    print (request.POST['first'])
    return redirect('/')