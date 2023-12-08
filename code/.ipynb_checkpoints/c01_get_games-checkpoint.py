
import pandas as pd
from urllib.error import HTTPError

from pathlib import Path
import time

# change to filepath for parent directory

fp_root = Path('c01_get_games.py').parent.absolute().parent.absolute()

dfs = []
years = range(2000, 2023 + 1)

for year in years:
  
  url = f'https://www.sports-reference.com/cfb/years/{year}-schedule.html'
  
  repeat_flag = True
  
  while repeat_flag:
  
    try:
    
      df_in = pd.read_html(io = url)[0]
      repeat_flag = False
    
    except HTTPError:
    
      time.sleep(5)

  print('.', end = '', flush = True)
  
  # format columns, keep relevant
  
  if year >= 2013:
  
    columns = ['rank', 'week', 'date', 'time', 'day', 'winner', 'pts_winner', 'field', 'loser', 'pts_loser', 'notes']
  
  else:
  
    columns = ['rank', 'week', 'date', 'day', 'winner', 'pts_winner', 'field', 'loser', 'pts_loser', 'notes']
  
  df_in.columns = columns
  
  df_in['year'] = year
  
  dfs.append(df_in)

df = pd.concat(dfs, ignore_index = True)

# drop rows that are header repetitions

df = df[df['week'].str.isnumeric()]

df.to_parquet(f'{fp_root}/data/raw/games.parquet')
