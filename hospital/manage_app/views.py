from django.shortcuts import render,redirect
from manage_app.models import pationt_list
from manage_app.forms import admission_form
# Create your views here.
def home_access(request):
    return render(request,'manage_app/home.html')
def form_access(request):
    if request.method=='POST':
        form=admission_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_page')
    else:
        form=admission_form()
    return render(request,'manage_app/admission.html',{'form':form})
def pationt_access(request):
    data=pationt_list.objects.all()
    return render(request,'manage_app/pationts.html',{'data':data})

