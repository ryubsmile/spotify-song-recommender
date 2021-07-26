# Add tracks csv to the model: Called only once for database migration
# ['valence,year,acousticness,artists,danceability,duration_ms,energy,explicit,id,instrumentalness,key,liveness,loudness,mode,name,popularity,release_date,speechiness,tempo\n']
import sys
import os
import pandas as pd
import sqlite3
import csv
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
"""
valence,year,acousticness,artists,danceability,duration_ms,energy,explicit,id,instrumentalness,key,liveness,loudness,mode,name,popularity,release_date,speechiness,tempo
"""
def addToModel():
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    a_file = open("/Users/sehwaryu/Documents/spotify-song-recommender/workspace/recommender/data.csv")
    rows = csv.reader(a_file)
    print(rows)
    cur.executemany("INSERT INTO recommender_tracks (valence,year,acousticness,artists,danceability,duration_ms,energy,explicit,track_id,instrumentalness,key,liveness,loudness,mode,track_name,popularity,release_date,speechiness,tempo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)

    cur.execute("SELECT * FROM recommender_tracks LIMIT 10")
    print(cur.fetchall())

    con.commit()
    con.close()


# def addToModel():
#     df = pd.read_csv('/Users/sehwaryu/Documents/spotify-song-recommender/workspace/recommender/data.csv')
#     print(df.head())
#     cnt = 0
#     for rows in df.itertuples():
#         print(rows[1])
#         cnt += 1
#         product = Tracks()  
#         product.valence = rows[1]
#         product.year = rows[2]  
#         product.acousticness = rows[3]  
#         product.artists = rows[4]  
#         product.danceability = rows[5]  
#         product.duration_ms = rows[6]  
#         product.energy = rows[7]  
#         product.explicit = rows[8]  
#         product.track_id = rows[9]  
#         product.instrumentalness = rows[10]  
#         product.key = rows[11]  
#         product.liveness = rows[12]  
#         product.loudness = rows[13]  
#         product.mode = rows[14]  
#         product.track_name = rows[15]  
#         product.release_date = rows[16]  
#         product.speechiness = rows[17]  
#         product.tempo = rows[18]  
#         print('save done')
#         product.save()  
#         if cnt > 5:
#             break
        