from github import Github
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def CSVCreate(token):
    # First create a Github instance:
    
    # using an access token
    g = Github(token)
    # Github Enterprise with custom hostname
    #g = Github(base_url="https://Mont9165/api/v3", login_or_token="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")

    # Then play with your Github objects:
    repositories = g.search_repositories(query='stars:>5000', sort='stars')
    count = 0
    repo_star = []
    star,fork,network,issue,subscriber,commit = [],[],[],[],[],[]

    for repo in repositories:
        if count < 500:
            star.append(repo.stargazers_count)
            fork.append(repo.forks_count)
            network.append(repo.network_count)
            issue.append(repo.open_issues_count)
            subscriber.append(repo.subscribers_count)
            commit.append(repo.get_commits().totalCount)
        else:
            break
        count += 1

    arr = np.array([star,fork,network,issue,subscriber,commit])
    df = pd.DataFrame(data=arr,index=['star','fork','network','issue','subscriber','commit'])
    df.to_csv('./star_analysis/star_data.csv')

def ColorMap(df):
    colormap = plt.cm.RdBu
    plt.figure()
    plt.title('Pearson Correlation of Features', y=1.05, size=15)
    sns.heatmap(df.astype(float).corr(),linewidths=0.1,vmax=1.0, 
                square=True, cmap=colormap, linecolor='white', annot=True)

def ScatterPlot(df):
    
    pass

class Main():
    token = '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'
    #CSVCreate(token)
    df_csv = pd.read_csv('./star_analysis/star_data.csv')
    df_csv_T = df_csv.T
    df = (df_csv_T.iloc[1:,0:]).astype('int32')
    #print(df)
    df_corr = df.corr()
    #print(df_corr)
    #print(df_corr[0][0])
    #ColorMap(df)
    #plt.savefig('./star_analysis/pearson correlation.png')
    for i in range(0,6):
        print((df_corr[0][i]*np.sqrt(498))/np.sqrt(1-df_corr[0][i]**2))
        pass
    pass