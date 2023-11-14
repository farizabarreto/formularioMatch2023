from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .inscricao import formInscricao
from .models import Inscrite

def home(request):
    form = formInscricao() #importa o ModelForm de inscricao
    return render(request, 'home.html', {'form': form}) # renderiza a página home com o a variável form criada
def sucesso(request):
    return render(request, 'sucesso.html') #renderiza a página sucesso
def processamento_form(request):
    form = formInscricao(request.POST) #coleta as informações do formulário
    ciencia = request.POST.get('ciencia', False)  #transfere o valor do campo BooleanField para Bool
    inscrites = Inscrite.objects.all().count() #armazena o número de inscrições já feitas no banco de dados

    if inscrites == 50:
        return HttpResponse("Sinto muito todas as vagas foram preenchidas") #verifica de o número máximo de vagas foi preenchido e retorna uma mensagem caso sim
    else:
        if form.is_valid(): #valida o formulário
            idade = int(form.data['idade']) #converte o campo idade para inteiro
            if idade < 18:
                return HttpResponse("Sinto muito, mas esse evento se destina a pesssoas com 18 anos ou mais")#verifica se a idade é menor de 18 e retorna mensagem
            elif form.data['uf'] != "SP" and form.data['uf'] != "sp":
                return HttpResponse("Sinto muito, esse evento se destina a pessoas residentes do estado de São Paulo") #verifica se a residência é no estado de São Paulo e retorna mensagem
            elif ciencia is False:
                return HttpResponse("É necessário marcar a caixa de seleção, atestando estar ciente do horário do evento") #verifica se a caixa de seleção foi marcada e retorna mensagem
            else:
                form.save() #caso passe em todas as verificações as informações são salvas
                return HttpResponseRedirect(reverse('sucesso')) #redirecionamento para uma página de confirmação da inscrição
        else:
            return HttpResponse("Erro no sistema, por favor tente novamente")

