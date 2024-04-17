from django.contrib import messages
from .forms import PessoaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pessoa
from django.db import IntegrityError
from django.utils.text import slugify
from django.db import IntegrityError
from .forms import UploadFileForm
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa

def home(request):
    return render(request, 'home.html')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             # Verificando a extensão do arquivo para determinar o tipo
#             if file.name.endswith('.csv'):
#                 # Se for um arquivo CSV, use o Pandas para ler os dados
#                 df = pd.read_csv(file, skiprows=[0])  # Pula a primeira linha (cabeçalho)
#             elif file.name.endswith('.xlsx'):
#                 # Se for um arquivo Excel, use o Pandas para ler os dados
#                 df = pd.read_excel(file, skiprows=[0])  # Pula a primeira linha (cabeçalho)
#             else:
#                 # Se a extensão do arquivo não for suportada, exiba uma mensagem de erro
#                 return render(request, 'error.html', {'error_message': 'Formato de arquivo não suportado. Apenas arquivos CSV e Excel são permitidos.'})

#             for index, row in df.iterrows():
#                 # Adicionar registro de depuração para verificar as colunas presentes em cada linha
#                 print(row)

#                 try:
#                     # Iterando sobre as linhas do DataFrame
#                     for index, row in df.iterrows():
#                         # Verificando se as colunas esperadas existem
#                         if 'Nome' in row and 'Idade' in row and 'Telefone' in row and 'Email' in row:
#                             # Criando uma instância de Pessoa com os dados do arquivo
#                             pessoa_data = {
#                                 'nome': row['Nome'] if 'Nome' in row else None,
#                                 'idade': row['Idade'] if 'Idade' in row else None,
#                                 'telefone': row['Telefone'] if 'Telefone' in row else None,
#                                 'email': row['Email'] if 'Email' in row else None,
#                             }
#                             # Criando uma instância de Pessoa com os dados do arquivo
#                             pessoa = Pessoa(**pessoa_data)
#                             # Salvando a instância no banco de dados
#                             pessoa.save()
#                         else:
#                             # Se alguma das colunas esperadas estiver faltando, exibir uma mensagem de erro
#                             return render(request, 'error.html', {'error_message': 'Alguma das colunas esperadas não foi encontrada no arquivo.'})
#                     # Se todas as instâncias de Pessoa forem criadas com sucesso, redirecionar para a página de sucesso
#                     return redirect('success')
#                 except KeyError:
#                     # Se uma chave não puder ser encontrada nas linhas do DataFrame, exibir uma mensagem de erro
#                     return render(request, 'error.html', {'error_message': 'Erro ao processar o arquivo.'})
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload_file.html', {'form': form})
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(file, skiprows=[0])
                except Exception as e:
                    return render(request, 'error.html', {'error_message': 'Erro ao ler o arquivo CSV: {}'.format(str(e))})
            elif file.name.endswith('.xlsx'):
                try:
                    df = pd.read_excel(file, skiprows=[0])
                except Exception as e:
                    return render(request, 'error.html', {'error_message': 'Erro ao ler o arquivo Excel: {}'.format(str(e))})
            else:
                return render(request, 'error.html', {'error_message': 'Formato de arquivo não suportado. Apenas arquivos CSV e Excel são permitidos.'})

            for index, row in df.iterrows():
                try:
                    if 'Nome' in row and 'Idade' in row and 'Telefone' in row and 'Email' in row:
                        pessoa_data = {
                            'nome': row['Nome'] if 'Nome' in row else None,
                           
                        }
                        pessoa = Pessoa(**pessoa_data)
                        pessoa.save()
                    else:
                        return render(request, 'error.html', {'error_message': 'Alguma das colunas esperadas não foi encontrada no arquivo.'})
                except Exception as e:
                    return render(request, 'error.html', {'error_message': 'Erro ao salvar dados do arquivo: {}'.format(str(e))})
            
            return redirect('listar_pessoas')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})


    

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome'].upper()  # Convertendo para maiúsculas
            cpf = form.cleaned_data['cpf']
            rg = form.cleaned_data.get('rg')  # Acessando o campo 'rg' de forma segura

            # Verificando se já existe uma pessoa com o mesmo nome, email, cpf ou rg
            if Pessoa.objects.filter(nome=nome).exists():
                form.add_error(None, 'Nome já cadastrado!')
            elif Pessoa.objects.filter(cpf=cpf).exists():
                form.add_error(None, 'CPF já cadastrado!')
            elif rg and Pessoa.objects.filter(rg=rg).exists():  # Verificando se 'rg' é válido
                form.add_error(None, 'RG já cadastrado!')
            else:
                try:
                    # Salvando pessoa com os dados normalizados
                    form.save()
                    messages.success(request, 'Pessoa cadastrada com sucesso!')
                    return redirect('cadastro_sucesso')
                except IntegrityError as e:
                    if 'UNIQUE constraint' in str(e):
                        form.add_error(None, 'Erro ao cadastrar pessoa: Já existe uma pessoa com esses dados.')
                    else:
                        form.add_error(None, 'Erro ao cadastrar pessoa: {}'.format(e))
    else:
        form = PessoaForm()
    return render(request, 'cadastro.html', {'form': form})

def cadastro_sucesso(request):
    return render(request, 'cadastro_sucesso.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})

def detalhes_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'detalhes_pessoa.html', {'pessoa': pessoa})

def editar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações da pessoa atualizadas com sucesso!')
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')
        return redirect('listar_pessoas')
    return render(request, 'confirmar_exclusao.html', {'pessoa': pessoa})
