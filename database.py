import sqlite3

def get_db():
    conn = sqlite3.Connection("gig_tracker.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db()
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

with open("schema.sql") as f:
    conn.executescript(f.read())

conn.close()
print("Database created")
'''
def add_song(connection,title, artist,*, lyrics=None, key=None, tempo=None,
             duration_seconds=None, genre=None, energy_level=None, 
             last_played_date=None, crowd_response_rating=None,difficulty=None,
             tags=None):
    with connection:
        cursor.execute("""INSERT INTO songs(title, artist, lyrics, key, tempo,
             duration_seconds, genre, energy_level,last_played_date, 
             crowd_response_rating,difficulty,tags) Values (:title, :artist, :lyrics, :key, :tempo,
             :duration_seconds, :genre, :energy_level,:last_played_date, 
             :crowd_response_rating,:difficulty,:tags)""", 
             {"title": title,
            "artist": artist,
            "lyrics": lyrics,
            "key": key,
            "tempo": tempo,
            "duration_seconds": duration_seconds,
            "genre": genre,
            "energy_level": energy_level,
            "last_played_date": last_played_date,
            "crowd_response_rating": crowd_response_rating,
            "difficulty": difficulty,
            "tags": tags, })
        return cursor.lastrowid

def add_setlist(connection, name, *, gig_date=None, location=None,
                notes= None, user_id=None):
    with connection:
        cursor.execute("""INSERT INTO setlists(name,gig_date,location,notes,user_id) 
        Values(:name, :gig_date, :location, :notes, :user_id)""", 
        {"name":name,
         "gig_date": gig_date,
         "location":location,
         "notes":notes,
         "user_id":user_id,})
        return cursor.lastrowid

def add_song_to_setlist(connection )

curr_id = add_song(connection, "Porque te vas de mi", "Ariel Camacho", key="G", tempo=120)
print(curr_id)

curr_setlist = add_setlist(connection, "Wedding", gig_date="01-01-2027")
print(curr_setlist)

cursor.execute("""SELECT * FROM setlists""")
for row in cursor.fetchall():
    print(dict(row))
    '''