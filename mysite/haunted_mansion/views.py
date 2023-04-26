from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def haunted_mansion(request):

    # return HttpResponse('haunted mansion')

    return render(request,'haunted_mansion.html')