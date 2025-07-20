import requests
import json

# Detalhes da issue que você quer consultar
owner = "prof-mrafaelbatista"  # Substitua pelo nome do dono do repositório prof-mrafaelbatista
repo = "projeto_a"  # Substitua pelo nome do repositório
issue_number = "1"  # Substitua pelo número da issue

# Seu token de acesso pessoal do GitHub (necessário para autenticação)
# Você pode criar um em https://github.com/settings/tokens
github_token = ""  # Substitua pelo seu token

# Endpoint da API do GitHub para listar as reações de uma issue
url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/reactions"

# Cabeçalhos da requisição, incluindo o token de autenticação
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

try:
    # Faz a requisição GET para a API do GitHub
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Levanta uma exceção para status de erro (4xx ou 5xx)

    # Analisa a resposta JSON
    reactions = response.json()

    # Extrai os logins dos usuários que reagiram
    logins_usuarios = set()
    for reaction in reactions:
        logins_usuarios.add(reaction["user"]["login"])

    # Imprime os logins dos usuários
    print(f"Logins dos usuários que reagiram à issue #{issue_number}:")
    for login in sorted(list(logins_usuarios)):
        print(login)

    print(list(logins_usuarios))

    with open("logins_usuarios.txt", "w") as f:
            for login in sorted(list(logins_usuarios)):
                f.write(login + "\n")



except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição para a API do GitHub: {e}")
except json.JSONDecodeError:
    print("Erro ao decodificar a resposta JSON da API do GitHub.")
except KeyError as e:
    print(f"Erro ao acessar chave esperada na resposta da API: {e}")