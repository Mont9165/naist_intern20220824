from github import Github
import matplotlib.pyplot as plt

# First create a Github instance:
token = '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'
# using an access token
g = Github(token)

# Github Enterprise with custom hostname
#g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

# Then play with your Github objects:
repositories = g.search_repositories(query='stars:>10000', sort='stars')
count = 0
repo_star_num = []
for repo in repositories:
    if count < 500:
        repo_star_num.append(repo.stargazers_count)
    else:
        break
    count += 1
    
plt.hist(repo_star_num)
plt.title('star_number')
plt.xlabel('star_num')
plt.ylabel('repo_num')
#plt.show()
plt.savefig('repo_star_histgram.png')