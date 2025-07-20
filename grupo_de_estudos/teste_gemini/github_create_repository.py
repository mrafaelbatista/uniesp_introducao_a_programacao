import requests

# Configurações
github_token = ""
org = "prof-mrafaelbatista"      # Substitua pelo nome da organização
repo_base = "251-sint-grupo"  # Nome base do repositório
quantidade = 26  # Quantos repositórios criar

url = f"https://api.github.com/orgs/{org}/repos"
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

for i in range(26, quantidade + 1):
    repo_name = f"{repo_base}{i}"
    data = {
        "name": repo_name,
        "private": False,
        "auto_init": True
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repositório '{repo_name}' criado com sucesso na organização '{org}'.")
        # Adiciona o time com permissão de push (leitura e escrita)
        team_slug = "251-sint"  # substitua pelo slug do time
        team_url = f"https://api.github.com/orgs/{org}/teams/{team_slug}/repos/{org}/{repo_name}"
        team_response = requests.put(
            team_url,
            headers=headers,
            json={"permission": "maintain"}  # "maintain" = manutenção (mais permissões que "push")
        )
        if team_response.status_code in [204, 201]:
            print(f"Time '{team_slug}' adicionado ao repositório '{repo_name}' com permissão de escrita.")
        else:
            print(f"Falha ao adicionar time: {team_response.status_code} - {team_response.text}")
    else:
        print(f"Falha ao criar repositório '{repo_name}': {response.status_code} - {response.text}")