import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import drawCourt

Harden_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&Plu'\
                'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'

Westbrook_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201566&Plu'\
                'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'

# Get the webpage containing the data
Harden_response = requests.get(Harden_url)
Westbrook_response = requests.get(Westbrook_url)
# Grab the headers to be used as column headers for our DataFrame
Harden_headers = Harden_response.json()['resultSets'][0]['headers']
Westbrook_headers = Westbrook_response.json()['resultSets'][0]['headers']
# Grab the shot chart data
Harden_shots = Harden_response.json()['resultSets'][0]['rowSet']
Westbrook_shots = Westbrook_response.json()['resultSets'][0]['rowSet']

Harden_shot_df = pd.DataFrame(Harden_shots, columns=Harden_headers)
Westbrook_shot_df = pd.DataFrame(Westbrook_shots, columns=Westbrook_headers)

# # View the head of the DataFrame and all its columns
# from IPython.display import display
# with pd.option_context('display.max_columns', None):
#     display(Harden_shot_df.head())

sns.set_style("white")
sns.set_color_codes()

plt.figure(figsize=(12,11))
# plot Westbrook's shots
plt.scatter(Westbrook_shot_df.LOC_X, Westbrook_shot_df.LOC_Y, color="b")
# plot Harden's shots
plt.scatter(Harden_shot_df.LOC_X, Harden_shot_df.LOC_Y, color="r")

drawCourt.draw_court()
# Adjust plot limits to just fit in half court
plt.xlim(-250,250)
# Descending values along th y axis from bottom to top in order to place the hoop by the top of plot
plt.ylim(422.5, -47.5)
# get rid of axis tick labels
plt.tick_params(labelbottom=False, labelleft=False)

plt.show()