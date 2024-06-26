from django import forms
from .models import Pessoa
from validate_docbr import CPF



class PessoaForm(forms.ModelForm):
    GENERO_CHOICES = [
        ('homem_cis', 'Homem Cis'),
        ('mulher_cis', 'Mulher Cis'),
        ('homem_trans', 'Homem Trans'),
        ('mulher_trans', 'Mulher Trans'),
        ('nao_binario', 'Não Binário'),
    ]

    PAIS_CHOICES = [
    ('Afeganistão', 'Afeganistão'),
    ('África do Sul', 'África do Sul'),
    ('Albânia', 'Albânia'),
    ('Alemanha', 'Alemanha'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antiga e Barbuda', 'Antiga e Barbuda'),
    ('Arábia Saudita', 'Arábia Saudita'),
    ('Argélia', 'Argélia'),
    ('Argentina', 'Argentina'),
    ('Arménia', 'Arménia'),
    ('Austrália', 'Austrália'),
    ('Áustria', 'Áustria'),
    ('Azerbaijão', 'Azerbaijão'),
    ('Bahamas', 'Bahamas'),
    ('Bangladexe', 'Bangladexe'),
    ('Barbados', 'Barbados'),
    ('Barém', 'Barém'),
    ('Bélgica', 'Bélgica'),
    ('Belize', 'Belize'),
    ('Benim', 'Benim'),
    ('Bielorrússia', 'Bielorrússia'),
    ('Bolívia', 'Bolívia'),
    ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'),
    ('Botsuana', 'Botsuana'),
    ('Brasil', 'Brasil'),
    ('Brunei', 'Brunei'),
    ('Bulgária', 'Bulgária'),
    ('Burquina Faso', 'Burquina Faso'),
    ('Burundi', 'Burundi'),
    ('Butão', 'Butão'),
    ('Cabo Verde', 'Cabo Verde'),
    ('Camarões', 'Camarões'),
    ('Camboja', 'Camboja'),
    ('Canadá', 'Canadá'),
    ('Catar', 'Catar'),
    ('Cazaquistão', 'Cazaquistão'),
    ('Chade', 'Chade'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Chipre', 'Chipre'),
    ('Colômbia', 'Colômbia'),
    ('Comores', 'Comores'),
    ('Congo-Brazzaville', 'Congo-Brazzaville'),
    ('Coreia do Norte', 'Coreia do Norte'),
    ('Coreia do Sul', 'Coreia do Sul'),
    ('Costa do Marfim', 'Costa do Marfim'),
    ('Costa Rica', 'Costa Rica'),
    ('Croácia', 'Croácia'),
    ('Cuba', 'Cuba'),
    ('Dinamarca', 'Dinamarca'),
    ('Dominica', 'Dominica'),
    ('Egito', 'Egito'),
    ('Emirados Árabes Unidos', 'Emirados Árabes Unidos'),
    ('Equador', 'Equador'),
    ('Eritreia', 'Eritreia'),
    ('Eslováquia', 'Eslováquia'),
    ('Eslovénia', 'Eslovénia'),
    ('Espanha', 'Espanha'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Estónia', 'Estónia'),
    ('Etiópia', 'Etiópia'),
    ('Fiji', 'Fiji'),
    ('Filipinas', 'Filipinas'),
    ('Finlândia', 'Finlândia'),
    ('França', 'França'),
    ('Gabão', 'Gabão'),
    ('Gâmbia', 'Gâmbia'),
    ('Gana', 'Gana'),
    ('Geórgia', 'Geórgia'),
    ('Granada', 'Granada'),
    ('Grécia', 'Grécia'),
    ('Guatemala', 'Guatemala'),
    ('Guiana', 'Guiana'),
    ('Guiné', 'Guiné'),
    ('Guiné Equatorial', 'Guiné Equatorial'),
    ('Guiné-Bissau', 'Guiné-Bissau'),
    ('Haiti', 'Haiti'),
    ('Honduras', 'Honduras'),
    ('Hungria', 'Hungria'),
    ('Iémen', 'Iémen'),
    ('Ilhas Marechal', 'Ilhas Marechal'),
    ('Índia', 'Índia'),
    ('Indonésia', 'Indonésia'),
    ('Irão', 'Irão'),
    ('Iraque', 'Iraque'),
    ('Irlanda', 'Irlanda'),
    ('Islândia', 'Islândia'),
    ('Israel', 'Israel'),
    ('Itália', 'Itália'),
    ('Jamaica', 'Jamaica'),
    ('Japão', 'Japão'),
    ('Jibuti', 'Jibuti'),
    ('Jordânia', 'Jordânia'),
    ('Kosovo', 'Kosovo'),
    ('Kuwait', 'Kuwait'),
    ('Laos', 'Laos'),
    ('Lesoto', 'Lesoto'),
    ('Letónia', 'Letónia'),
    ('Líbano', 'Líbano'),
    ('Libéria', 'Libéria'),
    ('Líbia', 'Líbia'),
    ('Listenstaine', 'Listenstaine'),
    ('Lituânia', 'Lituânia'),
    ('Luxemburgo', 'Luxemburgo'),
    ('Macedónia do Norte', 'Macedónia do Norte'),
    ('Madagáscar', 'Madagáscar'),
    ('Malásia', 'Malásia'),
    ('Malávi', 'Malávi'),
    ('Maldivas', 'Maldivas'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marrocos', 'Marrocos'),
    ('Maurícia', 'Maurícia'),
    ('Mauritânia', 'Mauritânia'),
    ('México', 'México'),
    ('Mianmar', 'Mianmar'),
    ('Micronésia', 'Micronésia'),
    ('Moçambique', 'Moçambique'),
    ('Moldávia', 'Moldávia'),
    ('Mónaco', 'Mónaco'),
    ('Mongólia', 'Mongólia'),
    ('Montenegro', 'Montenegro'),
    ('Namíbia', 'Namíbia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Nicarágua', 'Nicarágua'),
    ('Níger', 'Níger'),
    ('Nigéria', 'Nigéria'),
    ('Noruega', 'Noruega'),
    ('Nova Zelândia', 'Nova Zelândia'),
    ('Omã', 'Omã'),
    ('Países Baixos', 'Países Baixos'),
    ('Palau', 'Palau'),
    ('Panamá', 'Panamá'),
    ('Papua Nova Guiné', 'Papua Nova Guiné'),
    ('Paquistão', 'Paquistão'),
    ('Paraguai', 'Paraguai'),
    ('Peru', 'Peru'),
    ('Polónia', 'Polónia'),
    ('Portugal', 'Portugal'),
    ('Quénia', 'Quénia'),
    ('Quirguistão', 'Quirguistão'),
    ('Quiribáti', 'Quiribáti'),
    ('Reino Unido', 'Reino Unido'),
    ('República Centro-Africana', 'República Centro-Africana'),
    ('República Checa', 'República Checa'),
    ('República Democrática do Congo', 'República Democrática do Congo'),
    ('República Dominicana', 'República Dominicana'),
    ('Roménia', 'Roménia'),
    ('Ruanda', 'Ruanda'),
    ('Rússia', 'Rússia'),
    ('Salomão', 'Salomão'),
    ('Salvador', 'Salvador'),
    ('Samoa', 'Samoa'),
    ('Santa Lúcia', 'Santa Lúcia'),
    ('São Cristóvão e Neves', 'São Cristóvão e Neves'),
    ('São Marinho', 'São Marinho'),
    ('São Tomé e Príncipe', 'São Tomé e Príncipe'),
    ('São Vicente e Granadinas', 'São Vicente e Granadinas'),
    ('Seicheles', 'Seicheles'),
    ('Senegal', 'Senegal'),
    ('Serra Leoa', 'Serra Leoa'),
    ('Sérvia', 'Sérvia'),
    ('Singapura', 'Singapura'),
    ('Síria', 'Síria'),
    ('Somália', 'Somália'),
    ('Sri Lanca', 'Sri Lanca'),
    ('Suazilândia', 'Suazilândia'),
    ('Sudão', 'Sudão'),
    ('Sudão do Sul', 'Sudão do Sul'),
    ('Suécia', 'Suécia'),
    ('Suíça', 'Suíça'),
    ('Suriname', 'Suriname'),
    ('Tailândia', 'Tailândia'),
    ('Taiwan', 'Taiwan'),
    ('Tajiquistão', 'Tajiquistão'),
    ('Tanzânia', 'Tanzânia'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Togo', 'Togo'),
    ('Tonga', 'Tonga'),
    ('Trindade e Tobago', 'Trindade e Tobago'),
    ('Tunísia', 'Tunísia'),
    ('Turcomenistão', 'Turcomenistão'),
    ('Turquia', 'Turquia'),
    ('Tuvalu', 'Tuvalu'),
    ('Ucrânia', 'Ucrânia'),
    ('Uganda', 'Uganda'),
    ('Uruguai', 'Uruguai'),
    ('Usbequistão', 'Usbequistão'),
    ('Vanuatu', 'Vanuatu'),
    ('Vaticano', 'Vaticano'),
    ('Venezuela', 'Venezuela'),
    ('Vietname', 'Vietname'),
    ('Zâmbia', 'Zâmbia'),
    ('Zimbábue', 'Zimbábue'),
]


    genero = forms.ChoiceField(choices=GENERO_CHOICES, label='Gênero')
    pais_origem = forms.ChoiceField(choices=PAIS_CHOICES, label='País de Origem')
    
    # Campos adicionados
    status_migratorio = forms.CharField(max_length=100, required=False, label='Status Migratório')
    estado_residencia = forms.CharField(max_length=100, required=False, label='Estado de Residência')
    cidade_residencia = forms.CharField(max_length=100, required=False, label='Cidade de Residência')
    estado_civil = forms.CharField(max_length=100, required=False, label='Estado Civil')
    raca_cor = forms.CharField(max_length=100, required=False, label='Raça/Cor')
    escolaridade = forms.CharField(max_length=100, required=False, label='Escolaridade')
    area_formacao = forms.CharField(max_length=100, required=False, label='Área de Formação')
    nivel_portugues = forms.CharField(max_length=100, required=False, label='Nível de Português')
    carteira_trabalho = forms.CharField(max_length=100, required=False, label='Carteira de Trabalho')
    situacao_laboral = forms.CharField(max_length=100, required=False, label='Situação Laboral')
    renda_familiar_mensal = forms.DecimalField(required=False, label='Renda Familiar Mensal')
    faixa_renda = forms.CharField(max_length=100, required=False, label='Faixa de Renda')
    cpf = forms.CharField(max_length=11, label='CPF', widget=forms.TextInput(attrs={'placeholder': 'Digite apenas números'}))
    consentimento = forms.BooleanField(label='Ao clicar no botão cadastrar, Concorda com o Consentimento *', required=True)

    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'idade', 'cpf','genero', 'pais_origem', 'endereco_cep', 'endereco',
                  'bairro', 'cidade', 'estado', 'telefone', 'email', 'situacao_migratoria',
                  'atividade_servico_1', 'atividade_servico_2', 'atividade_servico_3', 'atividade_servico_4',
                  'atividade_servico_5', ]

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf_validator = CPF()

        if not cpf_validator.validate(cpf):
            raise forms.ValidationError('CPF inválido', code='invalid')

        return cpf
    

class UploadFileForm(forms.Form):
    # Defina o campo de arquivo para o formulário de upload de arquivo
    file = forms.FileField(label='Selecione um arquivo')
