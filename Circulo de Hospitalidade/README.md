# Circulo de Hospitalidade

Este é o README para a aplicação **reBuild**. Esta aplicação é um sistema de gerenciamento de cadastros, que permite adicionar, listar, editar e excluir informações acerca dos beneficiários da **ONG Círculos de Hospitalidade**.

## Pré-requisitos
- **Python 3.x**
- **Django 3.x**
Certifique-se de ter o Python e o Django instalados em sua máquina antes de prosseguir.

## Instalação
```bash
# Clone o repositório para o seu ambiente local:
git clone https://github.com/seu-usuario/circulo-de-hospitalidade.git
# Navegue até o diretório do projeto:
cd circulo-de-hospitalidade
# Instale as dependências:
pip install -r requirements.txt
# Execute as migrações do banco de dados:
python manage.py migrate
# Inicie o servidor de desenvolvimento:
python manage.py runserver
Acesse a aplicação em seu navegador através do seguinte link: 
http://localhost:8000/

Uso
Para cadastrar um novo beneficiário, acesse a página de cadastro através do link "Cadastrar Novo Beneficiário" na página inicial.
Para listar todos os beneficiários cadastrados, acesse a página "Listar Beneficiários já cadastrados".
Para editar ou excluir uma pessoa, acesse a página de detalhes do beneficiário e clique nos botões correspondentes.
Você também pode realizar o upload de arquivos clicando em "Upload de Arquivo" no header.