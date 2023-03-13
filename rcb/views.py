from django.shortcuts import render

# Create your views here.
def RCB(request):
    k={'name':'ABD'}
    return render(request,'CSK.html',context=k)