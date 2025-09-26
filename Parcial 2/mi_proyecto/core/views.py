from django.shortcuts import render, redirect
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm
from django.contrib import messages

def videos(request):
    videos = Video.objects.all()
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video agregado correctamente.')
            return redirect('videos')
    else:
        form = VideoForm()
    return render(request, 'core/videos.html', {'videos': videos, 'form': form})

def usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario agregado correctamente.')
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'core/usuarios.html', {'usuarios': usuarios, 'form': form})

def creditos(request):
    return render(request, 'core/creditos.html')
