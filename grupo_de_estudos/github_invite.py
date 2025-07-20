import requests

# Configurações
github_token = "" # Substitua pelo seu token
org = "prof-mrafaelbatista"      # Substitua pelo nome da organização
team_slug = "251-sint"       # Substitua pelo slug do time (nome em minúsculo, sem espaços)

with open("logins_usuarios.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

for username in usernames:
    url = f"https://api.github.com/orgs/{org}/teams/{team_slug}/memberships/{username}"
    response = requests.put(url, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Usuário {username} adicionado ao time {team_slug}.")
    else:
        print(f"Falha ao adicionar {username}: {response.status_code} - {response.text}")