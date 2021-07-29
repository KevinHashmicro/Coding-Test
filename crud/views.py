from crud.models import Mahasiswa, Task
from crud.controllers import doTask
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, ('home.html'))  

class TaskController:
    def newTask(request):
        return render(request, ('task/newTask.html'))

    def taskIndex(request):
        tsk = Task.objects.all()
        mhs = Mahasiswa.objects.all()
        return render(request, 'task/taskIndex.html', {'tsk' : tsk, 'mhs' : mhs})     

    def hshow(request,key):
        tsk = Task.objects.get(id = key)
        return render(request, 'task/taskShow.html', {'tsk':tsk})

    def clear(request, key):
        tsk = Task.objects.get(id=key)
        tsk.delete()
        messages.success(request, "Task was deleted!!!")
        return redirect('/task')

    def checkInput(request):
        tsk = Task()
        tsk.first = request.POST.get('first')
        tsk.second = request.POST.get('second')
        tsk.res = doTask(tsk.first, tsk.second)
        tsk.save()
        tsk = Task.objects.all()
        messages.success(request, "Task Done")
        return render(request, 'task/taskIndex.html', {'tsk' : tsk}) 


class MahasiswaController:
    def index(request):
        mhs = Mahasiswa.objects.all()
        return render(request, 'mahasiswa/index.html', {'mhs' : mhs})

    def create(request):
        return render(request, ('mahasiswa/create.html'))

    def store(request):
        mhs = Mahasiswa()
        mhs.nim = request.POST.get('nim')
        mhs.name = request.POST.get('name')
        mhs.email = request.POST.get('email')
        mhs.save()
        messages.success(request, "Mahasiswa was created!!!")
        return redirect('/mahasiswa/create')

    def show(request,key):
        mhs = Mahasiswa.objects.get(id = key)
        return render(request, 'mahasiswa/show.html', {'mhs':mhs})

    def edit(request, key):
        mhs = Mahasiswa.objects.get(id = key)
        return render(request, 'mahasiswa/edit.html', {'mhs':mhs})

    def update(request, key):
        print('in')
        mhs = Mahasiswa.objects.get(id= key)
        mhs.nim = request.POST.get('nim')
        mhs.name = request.POST.get('name')
        mhs.email = request.POST.get('email')
        mhs.save()
        messages.success(request, "Mahasiswa was updated!!!")
        return redirect('/mahasiswa')

    def delete(request, key):
        mhs = Mahasiswa.objects.get(id=key)
        mhs.delete()
        messages.success(request, "Mahasiswa was deleted!!!")
        return redirect('/mahasiswa')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'