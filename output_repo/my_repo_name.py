from github import Github

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
for repo in g.get_user().get_repos(type='owner'):
    print(repo.name)

