# CaseAutoU - Aplicação Web de Classificação de E-mails usando IA

## 🚀 Sobre a aplicação

Esta é uma aplicação web desenvolvida com HTML, CSS e Python (Flask) que utiliza Inteligência Artificial para **classificar e-mails** e **sugerir respostas automáticas**. O objetivo é ajudar os usuários a organizar suas caixas de entrada de forma prática e eficiente, diferenciando e-mails que requerem ações de e-mails que não precisam de atenção imediata.

A aplicação é capaz de:

- **Classificar e-mails em categorias predefinidas**:
  - **Produtivo**: e-mails que requerem ação ou resposta (ex.: solicitações de suporte, dúvidas, atualizações de casos).
  - **Improdutivo**: e-mails que não necessitam de ação imediata (ex.: newsletters, propagandas, notificações automáticas).

- **Sugerir respostas automáticas** para e-mails classificados como produtivos, facilitando a comunicação e economizando tempo.

---

## 💻 Tecnologias utilizadas

- **Frontend**: HTML, CSS  
- **Backend**: Python com Flask  
- **IA / NLP**: Modelos de linguagem para classificação e sugestão de respostas  

---

## 🛠 Funcionalidades

1. Interface simples e intuitiva para inserção de e-mails.
2. Classificação automática dos e-mails em produtivo ou improdutivo.
3. Sugestão de respostas automáticas baseadas no conteúdo do e-mail.
4. Organização visual com cards e histórico de e-mails processados.
5. Responsividade para diferentes tamanhos de tela.

## Pré-requisitos

1. Antes de começar, você precisa ter instalado:
Python 3.9+
pip (gerenciador de pacotes do Python)
Um editor de código (VS Code recomendado)

2. Clonar ou baixar o projeto
Se estiver no GitHub:
git clone https://github.com/seu-repositorio/CaseAutoU.git
cd CaseAutoU

3. Criar um ambiente virtual (recomendado)
python -m venv venv
Ativar o ambiente virtual:
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

4. Instalar dependências
pip install -r requirements.txt

5. Configurar a chave da API
Crie um arquivo .env na raiz do projeto.
Adicione sua chave da OpenAI nele:
OPENAI_API_KEY=sua_chave_aqui 

6. Rodar o servidor local
python app.py

7. Acessar no navegador
Abra: 👉 http://127.0.0.1:5000

A aplicação estará rodando localmente e pronta para classificar emails. 🎉

---
