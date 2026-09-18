from fastapi import FastAPI, HTTPException
import models as models
import database as database

app = FastAPI()

#landing page
@app.get("/")
def home():
    return {"message": "Hello World"}

#post to setlists
@app.post("/setlists")
def create_setlist(setlist: models.SetlistCreate):
    #open connection using func
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        #INSERT INTO THE TABLE
        cursor.execute(
            """INSERT INTO setlists(name ,gig_date,location,notes,user_id)
            Values (?,?,?,?,?)""", (setlist.name, setlist.gig_date, setlist.location,setlist.notes,setlist.user_id)
        )
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **setlist.model_dump()}
#get all setlists
@app.get("/setlists")
def get_all_setlists():
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM setlists""")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

#get a setlist using setlist.id
@app.get("/setlists/{setlist_id}")
def get_setlist(setlist_id : int):
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM setlists WHERE id = ?""", (setlist_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404,detail="Setlist not found")
    return dict(row)

#update a setlist
@app.put("/setlists/{setlist_id}")
def update_setlist(setlist_id: int, setlist:models.SetlistCreate):
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            """UPDATE setlists SET name=?, gig_date=?, location=?, notes=? WHERE
        id =?""", (setlist.name, setlist.gig_date, setlist.location,setlist.notes, setlist_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Setlist not found")
    conn.close()
    return {"id":setlist_id, **setlist.model_dump()}

#delete a setlist
@app.delete("/setlists/{setlist_id}")
def delete_setlist(setlist_id: int):
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        cursor.execute("""DELETE FROM setlists WHERE id=?""", (setlist_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code = 404, detail="Setlist not found")
    conn.close()
    return {"detail": f"Setlist {setlist_id} succesfully deleted"}



@app.get("/songs")
def get_all_songs():
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM songs""")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.post("/songs")
def create_song(song: models.SongCreate):
    #open connection using func
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        #INSERT INTO THE TABLE
        cursor.execute(
            """INSERT INTO songs(
                title,
                artist,
                lyrics,
                key,
                tempo,
                duration_seconds,
                genre,
                energy_level,
                last_played_date,
                crowd_response_rating,
                difficulty,
                tags,
                metadata_verified
                )
            Values (?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
            (song.title,
            song.artist,
            song.lyrics,
            song.key,
            song.tempo,
            song.duration_seconds,
            song.genre,
            song.energy_level,
            song.last_played_date,
            song.crowd_response_rating,
            song.difficulty,
            song.tags,
            song.metadata_verified)
            )
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **song.model_dump()}

@app.get("/songs/{song_id}")
def get_song(song_id : int):
    conn = database.get_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM songs WHERE id = ?""", (song_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404,detail="Song not found")
    return dict(row)

@app.put("/songs/{song_id}")
def update_song(song_id: int, song:models.SongCreate):
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            """UPDATE songs SET 
            title=?,
            artist=?,
            lyrics=?,
            key=?,
            tempo=?,
            duration_seconds=?,
            genre=?,
            energy_level=?,
            last_played_date=?,
            crowd_response_rating=?,
            difficulty=?,
            tags=?,
            metadata_verified=? WHERE
        id =?""", (
            song.title,
            song.artist,
            song.lyrics,
            song.key,
            song.tempo,
            song.duration_seconds,
            song.genre,
            song.energy_level,
            song.last_played_date,
            song.crowd_response_rating,
            song.difficulty,
            song.tags,
            song.metadata_verified,
            song_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Song not found")
    cursor.execute("SELECT * FROM songs WHERE id =?", (song_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)

@app.delete("/songs/{song_id}")
def delete_song(song_id: int):
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        cursor.execute("""DELETE FROM songs WHERE id=?""", (song_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code = 404, detail="Song not found")
    conn.close()
    return {"detail": f"Song {song_id} succesfully deleted"}

@app.patch("/songs/{song_id}/play")
def update_times_played(song_id: int):
    conn = database.get_db()
    cursor = conn.cursor()
    with conn:
        cursor.execute("""UPDATE songs SET times_played = times_played +1  WHERE id=?""", (song_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code = 404, detail="Song not found")
    conn.close()

    return {"detail": f"Song {song_id} times_played succesfully updated"}