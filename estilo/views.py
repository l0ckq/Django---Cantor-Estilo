from django.shortcuts import render, redirect, get_object_or_404
from .models import Estilo

def listar_estilos(request):
    estilos = Estilo.objects.all() # All -- puxa todos os dados do DB
    return render(request, 'listarEstilo.html', {'estilos':estilos})

def cadastrar_estilos(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Estilo.objects.create(nome=nome) # Create -- Cria uma instancia nova no DB
        return redirect('listar_estilos')
    return render(request, 'formEstilo.html')

def editar_estilos(request, id):
    estilos = get_object_or_404(Estilo, id=id)
    if request.method == "POST":
        estilos.nome = request.POST['nome']
        estilos.save()
        return redirect('listar_estilos')
    return render(request, 'formEstilo.html', {'estilos':estilos})

def excluir_estilos(request, id):
    estado = get_object_or_404(Estilo, id=id)
    if request.method == "POST":
        estado.delete()
        return redirect('listar_estilos')
    return render(request, 'confirmar_exclusaoEstilo.html', {'estado':estado})
