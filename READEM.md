# Circulo de Hospitalidade

Este é o README para a aplicação **reBuild**. Essa aplicação é um sistema de gerenciamento de cadastros, permitindo adicionar, listar, editar e excluir informações acerca dos Beneficiários da ONG Círculos de Hospitalidade.

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
Para cadastrar um novo Beneficiário, acesse a página de cadastro através do link "Cadastrar novo Beneficário" na página inicial.
Para listar todos os Beneficiários cadastrados, acesse a página "Listar Beneficiários já cadastrados".
Para editar ou excluir um Beneficiário já cadastrado, acesse a página de detalhes do Beneficiário e clique nos botões correspondentes.
Você também pode importar dados de um arquivo CSV ou Excel na página de upload de arquivo.
