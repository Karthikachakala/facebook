from django.shortcuts import render
from fb.models import create
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    obj=create.objects.all()
    return render(request,'post.html')



@login_required(login_url="/admin")
def create(request):
    if request.method=="POST":
        image=request.FILES.get('img')
        capt=request.POST.get('caption')
        obj=create(user=request.user,image=image,caption=capt)
        obj.save()
        
    return render(request,'home.html')
# Create your views here.
