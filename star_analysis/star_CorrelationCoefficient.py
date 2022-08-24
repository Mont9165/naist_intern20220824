from github import Github
import pandas as pd
import numpy as np

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
repositories = g.search_repositories(query='stars:>5000', sort='stars')
count = 0
repo_star = []
star,fork,network,issue,subscriber = [],[],[],[],[]

for repo in repositories:
    if count < 500:
        star.append(repo.stargazers_count)
        fork.append(repo.forks_count)
        network.append(repo.network_count)
        issue.append(repo.open_issues_count)
        subscriber.append(repo.subscribers_count)
    else:
        break
    count += 1

arr = np.array([star,fork,network,issue,subscriber])
dict = dict(star=star,)
df = pd.DataFrame(data=arr)
df.to_csv('star_sort_data.csv')
