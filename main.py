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

