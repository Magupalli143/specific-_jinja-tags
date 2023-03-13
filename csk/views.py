from django.shortcuts import render

# Create your views here.
def CSK(request):
    d={'name':'dhoni'}
    return render(request,'CSK.html',context=d)