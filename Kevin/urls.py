"""Kevin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from crud.views import MahasiswaController, SignUpView, TaskController, home
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('task', TaskController.taskIndex, name='tsk.taskIndex'), 
    path('task/newTask', TaskController.newTask, name='tsk.newTask'),
    path('task/checkInput', TaskController.checkInput, name='tsk.checkInput'),   
    path('task/<int:key>/show', TaskController.hshow, name="tsk.hshow"),
    path('task/<int:key>/delete', TaskController.clear, name="tsk.clear"),
    path('admin/', admin.site.urls),
    path('mahasiswa/', MahasiswaController.index, name="mhs.index"),
    path('mahasiswa/create/', MahasiswaController.create, name="mhs.create"),
    path('mahasiswa/store/', MahasiswaController.store, name="mhs.store"),
    path('mahasiswa/<int:key>/show', MahasiswaController.show, name="mhs.show"),
    path('mahasiswa/<int:key>/edit', MahasiswaController.edit, name="mhs.edit"),
    path('mahasiswa/<int:key>/update', MahasiswaController.update, name="mhs.update"),
    path('mahasiswa/<int:key>/delete', MahasiswaController.delete, name="mhs.delete"),

    path('', include('django.contrib.auth.urls')), # new
    path('signup/', SignUpView.as_view(), name='signup'),
]
