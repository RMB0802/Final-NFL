# %%
import pandas as pd
import random

# %%
def team_season_shuffle(season_year):
    links_df = pd.read_csv('team_links.csv',index_col=0)
    team_links_df = links_df['0'].apply(lambda x: x[:-8])
    team_links_df = team_links_df.apply(lambda x: x+str(season_year)+'.htm')
    random.shuffle(team_links_df)
    return team_links_df



