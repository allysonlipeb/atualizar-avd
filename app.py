import requests
from dotenv import load_dotenv
import os
from dados import data
load_dotenv()

# URL do endpoint
url = os.getenv("API_URL")

# Loop para enviar a solicitação para cada CPF
for entry in data:
    cpf = entry["cpf"]
    body = {
        "cpf": cpf,
        "quadrante_avd": entry["quadrante_avd"]
    }

    # Fazendo a solicitação POST
    response = requests.patch(f"{url}{cpf}", json=body)

    # Verificando o resultado de cada requisição
    if response.status_code == 200:
        print(f"CPF {cpf} atualizado com sucesso.")
    else:
        print(f"Erro ao atualizar CPF {cpf}: {response.status_code}, {response.text}")
