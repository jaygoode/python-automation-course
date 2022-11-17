import pandas as pd

# onThisDay = pd.read_html(
#     'https://www.bbc.com/sport/football/championship/scores-fixtures')

# print(len(onThisDay))

scoreCSV = pd.read_csv('https://football-data.co.uk/mmz4281/2223/E0.csv')


scoreCSV.rename(columns={'FTHG': 'home_goals'}, inplace=True)
print(scoreCSV)
