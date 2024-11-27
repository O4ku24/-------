from django.shortcuts import render
from .models import Users, Tasks


def home(request):
    return render(request=request, template_name='todo/home.html')


def registation(request):
    if request.method == 'GET':
        return render(request=request, template_name='todo/registration.html')
    
    if request.method == 'POST':
        print(request.POST)
        login = request.POST['login']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(pass1)
        print(pass2)
        if pass1 == pass2:
            new_user = Users.objects.create(login=login, password = pass1, tg_id = None)
        else:
            print('error password')
            return render(request=request, template_name='todo/registration.html')

        return render(request=request, template_name='todo/tasks.html', context=new_user.tg_id)


def tasks(request):
    if request.method == 'GET':
        data = []

        tasks_list = Tasks.objects.values()
        for task in tasks_list:
            data.append(task)

        return render(request=request, template_name='todo/tasks.html', context={'data':data})
    
    if request.method == 'POST':
        print(request.POST)
        user = request.POST['csrfmiddlewaretoken']
        print(user)
        title = request.POST['title']
        description = request.POST['description']
        dead_line = request.POST['deadline']

        new_task = Tasks.objects.create(title=title, description=description, deadline=dead_line, tg=user)

        return render(request=request, template_name='todo/tasks.html', context=new_task)
    

def auth(request):
    if request.method == 'GET':
        return render(request=request, template_name='todo/auth.html')
    
    if request.method == 'POST':
        return render(request=request)