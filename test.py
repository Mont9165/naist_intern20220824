from github import Github

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
repositories = g.search_repositories(query='forks:>50000', sort='forks')
count = 0
for repo in repositories:
    if count < 5:
        print(repo.get_commits().totalCount)
    else:
        break
    count += 1