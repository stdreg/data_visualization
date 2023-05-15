import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Status Code: {r.status_code}")

response = r.json()
print(f"Total Repos: {response['total_count']}")

repos = response['items']
print(f"Repos received: {len(repos)}")


print("\nSelected Infos about the first five repositorys:")
for repo in repos[0:10]:
    print(f"\nName: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")

