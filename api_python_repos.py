import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status Code: {r.status_code}")

response = r.json()
print(f"Total Repos: {response['total_count']}")

repos = response['items']
print(f"Repos received: {len(repos)}")

repo = repos[0]
print(f"Keys per Repo: {len(repo.keys())}")
for key in repo.keys():
    print(key)
