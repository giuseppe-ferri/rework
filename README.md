# RE:WORK IA

Agente de inteligência artificial integrado ao sistema **Rework/RBX**, capaz de responder perguntas em linguagem natural sobre clientes e chamados de suporte.

## O que o agente faz

Você digita uma pergunta como "Quais clientes mais abriram chamados em abril?" e o agente consulta automaticamente as APIs do sistema RBX, analisa os dados e responde em português.

Perguntas suportadas:
- Quais clientes mais abriram chamados em um período?
- Quantos chamados cada cliente abriu?
- Quais tópicos apareceram mais em um período?
- Quais chamados estão encerrados ou abertos?
- Quais causas mais aparecem nos encerramentos?
- Histórico de ocorrências de um ticket específico
- Dados cadastrais de um cliente pelo código

## Tecnologias

- **Python** + **Flask** — servidor da aplicação
- **LangChain** + **LangGraph** — orquestração do agente de IA
- **Groq (LLaMA 3.3)** — modelo de linguagem
- **Rework API** — middleware de integração com o RBX

## Pré-requisitos

- Python 3.10 ou superior
- Acesso à rede onde o Rework está hospedado (`http://192.168.0.124:8080`)
- Chave de API da Groq (gratuita em [console.groq.com](https://console.groq.com))

## Instalação

1. Clone o repositório e entre na pasta:
```bash
git clone https://github.com/seu-usuario/rbx-ai-agent.git
cd rbx-ai-agent
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install flask flask-cors python-dotenv requests langchain langchain-groq langchain-community langgraph
```

4. Crie o arquivo `.env` na raiz do projeto:
```env
GROQ_API_KEY=sua_chave_aqui
BASE_URL=http://192.168.0.124:8080
```

## Como usar

1. Inicie o servidor:
```bash
python app.py
```

2. Abra o arquivo `index.html` no navegador.

3. Digite sua pergunta no campo de texto e clique em **Enviar**.

## Estrutura do projeto# rework
