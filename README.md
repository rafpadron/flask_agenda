# 📅 Flask Agenda

Sistema de agendamento desenvolvido em Python com Flask, utilizando SQLAlchemy
para gerenciamento do banco de dados e um frontend em HTML/CSS.

## Funcionalidades
- Cadastro e gerenciamento de eventos/compromissos
- Persistência de dados com MySQL via SQLAlchemy
- Interface web responsiva

## Tecnologias
- Python
- Flask
- SQLAlchemy
- MySQL
- HTML / CSS

## Estrutura do projeto

flask_agenda/

├── models/      # Modelos do banco de dados
├── routes/      # Rotas da aplicação
├── templates/   # Páginas HTML
├── static/      # Arquivos estáticos (CSS, imagens)
├── utils/       # Funções auxiliares
└── app.py       # Arquivo principal

## Como executar
```bash
pip install -r requirements.txt
python app.py
```

## Aprendizados
Este projeto foi desenvolvido para praticar arquitetura MVC, integração com
banco de dados relacional e organização de código em Flask.
