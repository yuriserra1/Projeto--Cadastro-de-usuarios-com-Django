from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,"usuarios/home.html")

def usuarios(request):
    #Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.save()
    # Exibir todos os usuarios ja cadastrados em uma nova página
    usuarios = {
        "usuarios": Usuario.objects.all()
    }
    # Retornar os dados para a pagina do usuario
    return render(request,"usuarios/usuarios.html",usuarios)
