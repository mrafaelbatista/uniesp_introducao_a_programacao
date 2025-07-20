import requests

github_token = ""
org = "prof-mrafaelbatista"
repo_base = "251-sint-grupo"
quantidade = 1  # Quantos repositórios deletar

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

for i in range(1, quantidade + 1):
    repo_name = f"{repo_base}{i}"
    url = f"https://api.github.com/repos/{org}/{repo_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repositório '{repo_name}' deletado com sucesso.")
    else:
        print(f"Falha ao deletar '{repo_name}': {response.status_code} - {response.text}")