from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    u = User.objects.get(id=1)
    context = {
        'user':u,
    }

    return render(request,'OPA/index.html',context)