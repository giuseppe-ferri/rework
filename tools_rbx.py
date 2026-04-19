from dotenv import load_dotenv
load_dotenv()

import requests
from langchain.tools import tool
import os

BASE_URL = os.getenv('BASE_URL')

@tool
def get_client(codigo: str) -> str:
    """Get cadastral data of a specific client by their code."""
    resp = requests.get(f"{BASE_URL}/admin/rbx-clientes/{codigo}")
    return str(resp.json())

@tool
def list_clients(page: int = 0, size: int = 50) -> str:
    """List all registered clients with pagination."""
    resp = requests.get(f"{BASE_URL}/admin/rbx-clientes", params={"page": page, "size": size})
    return str(resp.json())

@tool
def search_tickets(
    opening_date_from: str = None,
    opening_date_to: str = None,
    client_code: str = None,
    closed: bool = None,
    topic: str = None,
    cause: str = None,
    page: int = 0,
    size: int = 100
) -> str:
    """Search tickets with filters. Dates must be in YYYY-MM-DD format.
    Use closed=True for closed tickets, closed=False for open tickets.
    Returns a list of tickets with client, topic, cause and status."""
    body = {"page": page, "size": size}
    if opening_date_from: body["aberturaDe"]   = opening_date_from
    if opening_date_to:   body["aberturaAte"]  = opening_date_to
    if client_code:       body["codigoCliente"] = client_code
    if closed is not None: body["encerrado"]   = closed
    if topic:             body["topico"]        = topic
    if cause:             body["causa"]         = cause
    resp = requests.post(f"{BASE_URL}/tickets/search", json=body)
    return str(resp.json())

@tool
def get_ticket_occurrences(ticket_number: str) -> str:
    """Get the full occurrence history of a ticket by its service number."""
    resp = requests.get(f"{BASE_URL}/tickets/{ticket_number}/ocorrências")
    return str(resp.json())

@tool
def list_causes() -> str:
    """List all available causes used for closing tickets."""
    resp = requests.get(f"{BASE_URL}/tickets/causas")
    return str(resp.json())

@tool
def list_topics() -> str:
    """List all available topics used in tickets."""
    resp = requests.get(f"{BASE_URL}/tickets/topicos")
    return str(resp.json())