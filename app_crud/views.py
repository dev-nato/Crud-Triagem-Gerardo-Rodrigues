from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'index.html')

def pacientes(request):
    novo_paciente = Pessoa()
    novo_paciente.nome = request.POST.get("nome")
    novo_paciente.temp = request.POST.get("temp")
    novo_paciente.peso = request.POST.get("kg")
    novo_paciente.pressao = request.POST.get("pa")
    novo_paciente.save()
    pacientes = { 'pacientes' : Pessoa.objects.all()}
    return render(request, 'lista/lista.html', pacientes)

def listar(request):
    return render(request, 'lista/lista.html', { 'pacientes' : Pessoa.objects.all()})
    
def edit(request, id):
    paciente = Pessoa.objects.get(id_pessoa=id)
    return render(request, 'alterar/alterar.html', {'paciente': paciente})

def savedit(request, id):
    novo_paciente = Pessoa()
    novo_paciente = Pessoa.objects.get(id_pessoa=id)
    novo_paciente.nome = request.POST.get("nome")
    novo_paciente.temp = request.POST.get("temp")
    novo_paciente.peso = request.POST.get("kg")
    novo_paciente.pressao = request.POST.get("pa")
    novo_paciente.save()
    paciente = {
        'pacientes': Pessoa.objects.all()
    }
    return redirect('/pacientes/', paciente)

def delete(request, id):
    paciente = Pessoa.objects.get(id_pessoa=id)
    paciente.delete()
    return redirect("/pacientes/", {'paciente': Pessoa.objects.all()})