from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL padrão para a página inicial
    path('cadastro/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('cadastro/sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
    path('listar/', views.listar_pessoas, name='listar_pessoas'),
    path('detalhes/<int:id>/', views.detalhes_pessoa, name='detalhes_pessoa'),
    path('editar/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('excluir/<int:id>/', views.excluir_pessoa, name='excluir_pessoa'),
    path('upload/', views.upload_file, name='upload_file'),
]
