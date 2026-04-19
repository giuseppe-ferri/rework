# app.py
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools_rbx import (
    get_client,
    list_clients,
    search_tickets,
    get_ticket_occurrences,
    list_causes,
    list_topics
)
import os

app = Flask(__name__)
CORS(app)

# Inicializa o modelo via LangChain
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Lista de tools disponíveis para o agente
tools = [
    get_client,
    list_clients,
    search_tickets,
    get_ticket_occurrences,
    list_causes,
    list_topics
]

# Cria o agente com LangGraph (abordagem moderna)
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="You are a helpful assistant that answers questions about clients and tickets. Always answer in Portuguese (pt-BR)."
)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    try:
        result = agent.invoke({
            "messages": [{"role": "user", "content": question}]
        })
        # Pega a última mensagem do agente como resposta final
        answer = result["messages"][-1].content
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)