from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Data
from .forms import AddData

# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = AddData(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            lm = fm.cleaned_data['lastname']
            lc = fm.cleaned_data['locality']
            ct = fm.cleaned_data['city']
            mb = fm.cleaned_data['mobile']
            em = fm.cleaned_data['email']
            alldata = Data(name=nm, lastname=lm, locality=lc, city=ct, mobile=mb, email=em)
            alldata.save()
            return HttpResponseRedirect('/')
    else:
        fm = AddData()
    displayData = Data.objects.all().order_by('name')
    return render(request, 'home.html', {'form':fm, 'alldata': displayData})


def update_data(request, id):
    if request.method == 'POST':
        update_object = Data.objects.get(pk=id)
        fm = AddData(request.POST, instance=update_object)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    # GET Method
    update_object = Data.objects.get(pk=id)
    fm = AddData(instance = update_object)           
    return render(request, 'update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        deleteObject = Data.objects.get(pk=id)
        deleteObject.delete()
        return HttpResponseRedirect('/')