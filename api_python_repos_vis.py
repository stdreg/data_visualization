from api_python_repos import GitHubApiPythonRepos
from plotly.graph_objs import Bar
from plotly import offline

githubapi = GitHubApiPythonRepos()
githubapi.load_repos()

names, stars = [], []
for repo_dict in githubapi.repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type': 'bar',
    'x': names,
    'y': stars,
}]
    
layout = {
    'title': 'Highest rated python repos on github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='pyhton_repos.html')

