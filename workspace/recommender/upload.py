# Add tracks.csv to the model: Called only once for database migration
import sys
import os
import sqlite3
import csv
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

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