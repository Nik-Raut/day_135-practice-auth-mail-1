from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm

def homeview(request):
    template_name='FrontEndApp/base.html'
    context={}
    return render(request,template_name,context)


@login_required(login_url='login')
def infoview(request):
    template_name='FrontEndApp/info.html'
    context={}
    return render(request,template_name,context)

@login_required(login_url='login')
def addStudent(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    template_name='FrontEndApp/addStudent.html'
    context={'form':form}
    return render(request,template_name,context)