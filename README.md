# CRUD com Flask
![Static Badge](https://img.shields.io/badge/status-Active-gren?style=for-the-badge)

## 📄 Descrição

Este projeto é um exemplo simples de CRUD (Create, Read, Update, Delete) utilizando o microframework Flask em Python. Ele permite criar, visualizar, atualizar e excluir tarefas através de requisições HTTP. Esse projeto foi desenvolvido na aula de **Desenvolvimento de APIs com Flask** 

## ⚙️ Funcionalidades

- **Criar Tarefa:**  Adiciona uma nova tarefa à lista.
- **Visualizar Todas as Tarefas:** Retorna todas as tarefas cadastradas.
- **Visualizar uma Tarefa Específica:** Exibe os detalhes de uma tarefa pelo seu ID.
- **Atualizar Tarefa:** Modifica as informações de uma tarefa existente.
- **Deletar Tarefa:** Remove uma tarefa da lista.

## 💻 Tecnologias Utilizadas

- **Python 3.11**: Linguagem utilizada para o desenvolvimento do jogo.
- **Flask 2.3.0**: Framework de desenvolvimento web utilizado para criar a aplicação e gerenciar rotas HTTP.

## 🚀 Instalando e Rodando o Projeto

1. Clone este repositório: `git@github.com:hi-giih/CRUD-com-o-Flask.git`
2. Acesse o diretório do projeto: `cd CRUD-com-o-Flask`
3. Crie um ambiente virtual (opcional, mas recomendado):

          python -m venv venv

4. Ative o ambiente virtual:

        Windows: venv\Scripts\activate

        Linux/Mac: source venv/bin/activate

5. Instale as dependências:

        pip install flask

6. Execute o projeto:

        python app.py

    O servidor estará disponível em: http://127.0.0.1:5000

## 🔧 Futuras Melhorias

- Implementação de persistência de dados com um banco de dados (SQLite, PostgreSQL, etc.).
- Autenticação e autorização para maior segurança.
- Validações mais robustas nas requisições.
- Interface gráfica com HTML/CSS para interação com o usuário.

## 📜 Licença 

Este projeto não está sob nenhuma licença.
