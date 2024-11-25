from django.shortcuts import render


def home(request):
    return render(request=request, template_name='todo/home.html')

def registation(request):
    if request.method == 'GET':
        return render(request=request, template_name='todo/registration.html')

def tasks(request):
    if request.method == 'GET':
        return render(request=request, template_name='todo/tasks.html')
    
def auth(request):
    if request.method == 'GET':
        return render(request=request, template_name='todo/auth.html')