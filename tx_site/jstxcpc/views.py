from django.shortcuts import render

# Create your views here.

def tx_home(request):
    return render(request,'index.html',{})

