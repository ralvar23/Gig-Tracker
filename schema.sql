CREATE TABLE IF NOT EXISTS songs(
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, 
    artist TEXT, 
    lyrics TEXT,
    key TEXT, 
    tempo INTEGER,
    duration_seconds INTEGER,
    genre TEXT,
    energy_level INTEGER, -- 1-10
    times_played INTEGER NOT NULL DEFAULT 0,
    last_played_date TEXT,
    crowd_response_rating INTEGER, -- 1-10
    difficulty INTEGER, -- 1-10
    tags TEXT,
    metadata_verified INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS setlists(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gig_date TEXT,
    location TEXT,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
    );

CREATE TABLE IF NOT EXISTS setlist_songs(
    id INTEGER PRIMARY KEY,
    setlist_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    position INTEGER,
    FOREIGN KEY (setlist_id) REFERENCES setlists(id),
    FOREIGN KEY (song_id) REFERENCES songs(id)
    );


CREATE TABLE IF NOT EXISTS chord_charts(
    id INTEGER PRIMARY KEY,
    song_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (song_id) REFERENCES songs(id)
    );


CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
