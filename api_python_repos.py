import requests

class GitHubApiPythonRepos:
    def __init__(self):
        self.repo_dicts = {}

    def load_repos(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url,headers=headers)
        print(f"Status Code (API-Call): {r.status_code}")
        response = r.json()    
        self.repo_dicts = response['items']        
    
    def print_repo_infos(self):
        print("\nSelected Infos about the repositorys:")
        for repo in self.repo_dicts:
            print(f"\nName: {repo['name']}")
            print(f"Owner: {repo['owner']['login']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"Repository: {repo['html_url']}")
            print(f"Created: {repo['created_at']}")
            print(f"Updated: {repo['updated_at']}")
            print(f"Description: {repo['description']}")

