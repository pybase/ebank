from django.contrib import messages
from django.shortcuts import render

from bank_app.models import Banking


# Create your views here.
def index(request):
    banking=Banking.objects.all()
    return render(request,'index.html',{'banking':banking})


def detail(request):

    return render(request,'detail.html')

def form(request):
    name='Fill the Form'

    return render(request,'form.html',{'name':name})