from django.db import models
from validate_docbr import CPF
from datetime import datetime
from datetime import date  # Adicione esta linha
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Defina os campos related_name para evitar colisões de acessadores reversos
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True, verbose_name='user permissions')

    class Meta:
        verbose_name = 'Refugiado'
        verbose_name_plural = 'Refugiados'



class Pessoa(models.Model):
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


    ATIVIDADE_CHOICES = [
        ('', 'Selecione...'),
        ('Acesso a Direitos', 'Acesso a Direitos'),
        ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'),
        ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'),
        ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'),
        ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'),
        ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'),
        ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'),
        ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'),
        ('Aulas de Português', 'Aulas de Português'),
        ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'),
        ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)'),
    ]

    ATIVIDADE_CHOICES = [
        ('', 'Selecione...'),
        ('Acesso a Direitos', 'Acesso a Direitos'),
        ('Acesso a Direitos (Assistência Social)', 'Acesso a Direitos (Assistência Social)'),
        ('Acesso a Direitos (Documentação para familiares)', 'Acesso a Direitos (Documentação para familiares)'),
        ('Acesso a Direitos (Educação)', 'Acesso a Direitos (Educação)'),
        ('Acesso a Direitos (Outros apoios com documentação)', 'Acesso a Direitos (Outros apoios com documentação)'),
        ('Acesso a Direitos (Saúde)', 'Acesso a Direitos (Saúde)'),
        ('Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)', 'Acesso a Direitos (Trabalho - SINE, carteira de trabalho, direitos trabalhistas, previdência social)'),
        ('Apoio com trabalho (preparo de currículo e vagas de trabalho)', 'Apoio com trabalho (preparo de currículo e vagas de trabalho)'),
        ('Aulas de Português', 'Aulas de Português'),
        ('Cursos de informática e tecnologia', 'Cursos de informática e tecnologia'),
        ('Regularização migratória (apoio com renovação ou solicitação de documentos)', 'Regularização migratória (apoio com renovação ou solicitação de documentos)'),
    ]
    
    nome_completo = models.CharField(max_length=100,  verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    idade = models.IntegerField(null=True, blank=True, verbose_name='Idade')
    cpf = models.CharField(max_length=11, default='', unique=True, verbose_name='CPF', help_text='Digite apenas números')
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, default='Outro', verbose_name='Gênero')
    pais_origem = models.CharField(max_length=100, choices=PAIS_CHOICES, default="Desconhecido", verbose_name='País de Origem')
    endereco_cep = models.CharField(max_length=9, default='', verbose_name='Endereço Residencial - CEP')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço Residencial (Nome da rua e número da casa)')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estado')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    situacao_migratoria = models.CharField(max_length=100, blank=True, null=True, verbose_name='Situação Migratória')
    atividade_servico_1 = models.CharField(max_length=100, choices=ATIVIDADE_CHOICES, blank=True, null=True, verbose_name='Atividade/Serviço Solicitado 1')
    atividade_servico_2 = models.CharField(max_length=100, choices=ATIVIDADE_CHOICES, blank=True, null=True, verbose_name='Atividade/Serviço Solicitado 2')
    atividade_servico_3 = models.CharField(max_length=100, choices=ATIVIDADE_CHOICES, blank=True, null=True, verbose_name='Atividade/Serviço Solicitado 3')
    atividade_servico_4 = models.CharField(max_length=100, choices=ATIVIDADE_CHOICES, blank=True, null=True, verbose_name='Atividade/Serviço Solicitado 4')
    atividade_servico_5 = models.CharField(max_length=100, choices=ATIVIDADE_CHOICES, blank=True, null=True, verbose_name='Atividade/Serviço Solicitado 5')

    # Campos adicionados
    status_migratorio = models.CharField(max_length=100, blank=True, null=True, verbose_name='Status Migratório')
    estado_residencia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estado de Residência')
    cidade_residencia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade de Residência')
    estado_civil = models.CharField(max_length=100, blank=True, null=True, verbose_name='Estado Civil')
    raca_cor = models.CharField(max_length=100, blank=True, null=True, verbose_name='Raça/Cor')
    escolaridade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Escolaridade')
    area_formacao = models.CharField(max_length=100, blank=True, null=True, verbose_name='Área de Formação')
    nivel_portugues = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nível de Português')
    carteira_trabalho = models.CharField(max_length=100, blank=True, null=True, verbose_name='Carteira de Trabalho')
    situacao_laboral = models.CharField(max_length=100, blank=True, null=True, verbose_name='Situação Laboral')
    renda_familiar_mensal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Renda Familiar Mensal')
    cpf_valido = models.BooleanField(default=False, verbose_name='CPF Válido')
    faixa_renda = models.CharField(max_length=100, blank=True, null=True, verbose_name='Faixa de Renda')

    def save(self, *args, **kwargs):
        # Calcula a idade com base na data de nascimento
        if self.data_nascimento:
            today = date.today()
            self.idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        # Valida o CPF
        if self.cpf:
            cpf = CPF()
            self.cpf_valido = cpf.validate(self.cpf)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name_plural = 'Pessoas'