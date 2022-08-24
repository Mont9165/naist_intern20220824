from github import Github
import seaborn
import matplotlib.pyplot as plt

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
repositories = g.search_repositories(query='language:python, stars:>5000', sort='stars')
count = 0
repo_star = []
for repo in repositories:
    if count < 500:
        repo_star.append(repo.stargazers_count)
    else:
        break
    count += 1

seaborn.histplot(repo_star)
plt.show()
plt.savefig("py_repo_star_histgram.png")