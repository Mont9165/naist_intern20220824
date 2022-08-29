from github import Github
import matplotlib.pyplot as plt

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
repositories = g.search_repositories(query='forks:>5000', sort='forks')
count = 0
repo_star = []
for repo in repositories:
    if count < 500:
        repo_star.append(repo.forks_count)
    else:
        break
    count += 1

plt.hist(repo_star_num)
plt.title('fork_number')
plt.xlabel('fork_num')
plt.ylabel('repo_num')
#plt.show()
plt.savefig('repo_fork_histgram.png')
