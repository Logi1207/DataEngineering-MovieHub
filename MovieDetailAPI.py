import requests
import csv
import time
import pandas as pd
from sqlalchemy import create_engine

header_data = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWY5YzYzNGMwMWIyZjA4ZmI0MDNkZWExNzdiOTIyNSIsInN1YiI6IjY1ZmU5ZTc2MDQ3MzNmMDE3ZGVjNjBmNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mvfphI1NIKujcbUUTZ0-dX9pN0sefVmbdj3uwMEHsj0" 
  }

### API Data Extraction:
print("Extracting data....")
csv_data = open("./MovieDetail.csv", 'a', encoding='utf-8', newline='')
page=1
while page<=100:
    print('Extracting page : {page}...')
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

    try:
        response = requests.get(url, headers=header_data)
        json_data = response.json()['results']
        title_names = json_data[0].keys()
        csv_writer = csv.DictWriter(csv_data, fieldnames=title_names)
        if page==1:
            csv_writer.writeheader()
        for val in json_data: 
            csv_writer.writerow(val)
        page=page+1
    except Exception as e:
        print(f'error fetching,{e}')
        time.sleep(1)
        page=page
csv_data.close()
print('Extracted data!')

### Title filtering with 'S' and 'H':
df = pd.read_csv('./MovieDetail.csv')
print("Filtering the titles....")
filtered_data = df[df['title'].str.startswith(('S', 'H'))]
filtered_data.to_csv('./ListOFSnH.csv', index=False)
print("Filtered the movies!")

### Database connection:
df = pd.read_csv('./ListOFSnH.csv')
selectedCols = df[['id','title', 'overview','popularity','release_date','vote_average','vote_count']]
renameSelectedCols = {'id':'movieId', 'release_date': 'releaseDate', 'vote_average': 'rating', 'vote_count':'voteCount'}
selectedCols = selectedCols.rename(columns=renameSelectedCols)
selectedCols['firstLetter'] = selectedCols['title'].str[0]
engine = create_engine('mysql+mysqlconnector://root:Logi%40mysql@localhost:3306/InviciblClouds')

try:
    selectedCols.to_sql(name='moviedetails', con=engine, if_exists='append', index=False, method='multi', chunksize=1000)
    print('Data loaded successfully!')
except Exception as e:
    print(f'Error loading data:{e}')