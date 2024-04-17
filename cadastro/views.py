from django.contrib import messages
from .forms import PessoaForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from django.db import IntegrityError
from django.utils.text import slugify
from .forms import UploadFileForm
import pandas as pd
import csv


def home(request):
    return render(request, 'home.html')


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

            success_count = 0
            error_messages = []

            for index, row in df.iterrows():
                pessoa_form = PessoaForm(row)
                if pessoa_form.is_valid():
                    try:
                        pessoa_form.save()
                        success_count += 1
                    except Exception as e:
                        error_messages.append(f'Erro ao salvar dados da linha {index + 2}: {str(e)}')
                else:
                    error_messages.append(f'Erro na linha {index + 2}: {pessoa_form.errors}')

            if error_messages:
                return render(request, 'error.html', {'error_messages': error_messages})
            else:
                return render(request, 'success.html', {'success_message': f'{success_count} registros foram adicionados com sucesso.'})
                

    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

    

from django.urls import reverse

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            nome_completo = form.cleaned_data['nome_completo'].upper()  # Convertendo para maiúsculas
            cpf = form.cleaned_data['cpf']
            rg = form.cleaned_data.get('rg')  # Acessando o campo 'rg' de forma segura

            # Verificando se já existe uma pessoa com o mesmo nome, email, cpf ou rg
            if Pessoa.objects.filter(nome_completo=nome_completo).exists():

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
                    # Redirecionando para a página que lista todas as pessoas cadastradas
                    return redirect('listar_pessoas')
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
