from django.test import TestCase

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
                    # Adicione instruções de impressão para depuração
                    print('Lendo linha do arquivo:', row)

                    pessoa_data = {
                        'nome': row['Nome'] if 'Nome' in row else None,
                        'cpf': row['CPF'] if 'CPF' in row else None,
                        'data_nascimento': row['Data de Nascimento'] if 'Data de Nascimento' in row else None,
                        'genero': row['Gênero'] if 'Gênero' in row else None,
                        'pais_origem': row['País de Origem'] if 'País de Origem' in row else None,
                        'endereco_cep': row['Endereço Residencial - CEP'] if 'Endereço Residencial - CEP' in row else None,
                    }

                    print('Dados da pessoa:', pessoa_data)

                    pessoa = Pessoa(**pessoa_data)
                    pessoa.save()
                except Exception as e:
                    return render(request, 'error.html', {'error_message': 'Erro ao salvar dados do arquivo: {}'.format(str(e))})
            
            return redirect('listar_pessoas')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})


