from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def master(request):
    return render(request,'master.html')
    
def carpool(request):
    return render(request,'carpool.html')

def test(request):
    return render(request,'test.html')