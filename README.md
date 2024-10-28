# paralimpicc_social
A Rede Social Paralímpica é uma plataforma web desenvolvida com Django, que permite a interação e o engajamento entre atletas, patrocinadores e torcedores da comunidade paralímpica.

## Funcionalidades Implementadas

1. **Autenticação de Usuários**:
   - Modelo de usuário customizado com campos adicionais para atletas e patrocinadores.
   - Registro e login de usuários.

2. **Perfil de Atleta**:
   - Informações detalhadas sobre o atleta, como classe funcional, modalidades e conquistas.
   - Registro de eventos futuros e mídias relacionadas ao atleta.
   - Ranking e sistema de medalhas.

3. **Conexão com Patrocinadores**:
   - Modelo de perfil de patrocinador com informações da empresa.
   - Sistema de solicitação de patrocínio entre atletas e patrocinadores.
   - Funcionalidade de seguir/deixar de seguir atletas e patrocinadores.

4. **Eventos e Competições**:
   - Criação e gerenciamento de eventos relacionados à comunidade paralímpica.
   - Inscrição de atletas em eventos e registro de resultados.

5. **Feed de Atividades**:
   - Publicação de posts com texto, imagens e tags.
   - Funcionalidade de curtir e comentar posts.
   - Busca avançada de posts e atletas.

6. **Sistema de Notificações**:
   - Criação de notificações quando um usuário curte ou comenta um post.
   - Exibição da lista de notificações para o usuário.
   - Opção de marcar todas as notificações como lidas.

7. **Conteúdo Inspiracional e Educacional**:
   - Publicação de artigos e webinars relacionados à comunidade paralímpica.
   - Inscrição de usuários em webinars.

## Tecnologias Utilizadas

- Python 3.9
- Django 3.2
- PostgreSQL
- Bootstrap 5

## Estrutura do Projeto

O projeto está organizado da seguinte forma:
paralimpic_social/
├── accounts/
├── events/
├── feed/
├── notifications/
├── sponsors/
├── content/
├── paralimpic_social/
└── templates/


Cada aplicação (app) é responsável por uma parte específica da funcionalidade do sistema.

## Configuração e Execução

1. Crie um ambiente virtual e ative-o:

python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate


2. Instale as dependências:

pip install -r requirements.txt


3. Crie o banco de dados PostgreSQL e atualize as configurações em `paralimpic_social/settings.py`.

4. Aplique as migrações:

python manage.py migrate


5. Inicie o servidor de desenvolvimento:

python manage.py runserver


6. Acesse a aplicação em `http://localhost:8000/`.
