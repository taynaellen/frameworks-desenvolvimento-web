# Frameworks_para_Desenvolvimento_Web

Avaliações:
- Portifólio que inclua tudo que foi desenvollvido durante a Unidade Curricular (Prazo: 12/02/2025)
- Projeto funcional individual
- Aplicação prática individual ao vivo ao lado do professor (Prazo: 22/01/2025)

Linguagem de programação: Python (no mínimo a versão 3.11)

Conhecimentos requisitados:
- Criar ambiente virtual em python
- Extensões: python ven
- Estar ambientado com sistema operacional linux
- Instalar pacotes
- Nunca inserir código na pasta do ambiente virtual
- Gerenciar o arquivo requeriment.txt


Comandos para criar ambiente virtual:
python -m venv nome_do_ambiente_virtual 
nome_do_ambiente_virtual/Scripts/activate

Dependências para instalar:
- flask sqlalchemy
- numpy (pip install numpy)

Sites recomendados:
- pypi (para seguir instruções para instalar dependências)

Padrões:
- Variáveis e funções declaradas em inglês
- Snake case


30/10/2024
Instalar Flask:
- $ pip install Flask

Programação reativa: funciona com base em requisição e resposta. O Flask concilia isto. Toda programação web funciona com base em request e response.

Pesquisar sobre o tipo de variável especial em python em que o nome da variável e o seu valor é a mesma coisa

Pesquisar sobre rotas e como selecionar portas


Protótipo dos trabalhos para o dia 20/11/2024

Atividade 1 - Criar uma rota para uma pégina web com a tag canvas que permite o usuário deslocar uma imagem para direita para esquerda com o teclado

Atividade 2 - Criar uma rota que permita o usuário procurar uma imagem da webcam

Atividade 3 - Criar uma rota com a pagina web que exiba uma tabela, sem usar table, de 997 linhas e 5 colunas
coluna 1: id
2 coluna nome
3 sobrenome
4 email
5 ações

Atividade 4 - Crie uma rota com 3 links, para a atividades anteriores estilizadas e -> bonitas <-

Atividade 5 - Crie 6 rotas, estilizadas, sendo que cada rota deve conter o curriculo de 1 integrante do grupo do preojeto



06/11/2024
- render_template

Atividades
1 - Considerando um usuário e uma senha moncados, faça uma página de autentificação que retorne uma mensagem de boas vindas de acordo com o horário da tentativa de acesso, caso a autentificação for bem sucedida.

2 - Limite as tentativas de autenfiticação da página da atividade 1 em duas vezes.

3 - Estilizar a página de forma bonita.

4 - Escreva um script pyhton que gere automaticamente um template html contendo um formulário para input de dados. Os campos que devem conter no formulário devem ser gerados por u  framework.

5 - Após gerar o template, faça com que seja construída automaticamente uma rota que permita acessa-lo.


Tarefa
Crie uma classe em python que encapsula e valida dados de usuário e desenvolva uma função de autentificação, isto é, precisa haver uma sessão.

