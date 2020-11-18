# Dropping Existing Tables 
songplays_table_drop = " DROP TABLE IF EXISTS songplays "
users_table_drop = " DROP TABLE IF EXISTS users "
songs_table_drop = " DROP TABLE IF EXISTS songs "
artists_table_drop = " DROP TABLE IF EXISTS artists "
time_table_drop = " DROP TABLE IF EXISTS time "

# Creating Tables
songplays_table_create = (
        """
        CREATE TABLE songplays (
            songplay_id SERIAL NOT NULL PRIMARY KEY,
            start_time TIMESTAMP NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            level VARCHAR(255) NOT NULL,
            song_id VARCHAR(255) NOT NULL,
            artist_id VARCHAR(255) NOT NULL,
            session_id VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            user_agent VARCHAR(255) NOT NULL
        )
        """)

users_table_create = (
        """
        CREATE TABLE users (
            user_id VARCHAR(255) NOT NULL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            gender VARCHAR(255) NOT NULL,
            level VARCHAR(255) NOT NULL
        )
        """)

songs_table_create = (
        """
        CREATE TABLE songs (
            song_id VARCHAR(255) NOT NULL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            artist_id VARCHAR(255) NOT NULL,
            year INT NOT NULL,
            duration TIMESTAMP NOT NULL
        )
        """)

artists_table_create = (
        """
        CREATE TABLE artists (
            artist_id VARCHAR(255) NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            latitude INT NOT NULL,
            longitude INT NOT NULL
        )
        """)

time_table_create = (
        """
        CREATE TABLE time (
            start_time TIMESTAMP NOT NULL ,
            hour INT NOT NULL,
            week INT NOT NULL,
            month INT NOT NULL,
            year INT NOT NULL,
            weekday INT NOT NULL
        )
        """)

# Inserting Records
songplays_table_insert = (
    """
    INSERT INTO songplays(
        songplay_id ,
        start_time ,
        user_id ,
        level ,
        song_id ,
        artist_id ,
        session_id ,
        location ,
        user_agent 
    )
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
    """
)

users_table_insert = (
    """
    INSERT INTO songplays(
        user_id, 
        first_name, 
        last_name, 
        gender, 
        level
    )
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (user_id) DO UPDATE 
        SET level = EXCLUDED.level
    """
)

songs_table_insert = (
    """
    INSERT INTO songplays(
        song_id, 
        title, 
        artist_id, 
        year, 
        duration
    )
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING
    """
)

artists_table_insert = (
    """
    INSERT INTO songplays(
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude
    )
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (artist_id) DO NOTHING
    """
)

time_table_insert = (
    """
    INSERT INTO songplays(
        start_time,
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday
    )
    VALUES(%s,%s,%s,%s,%s)
    ON CONFLICT (start_time) DO NOTHING
    """
)

# Finding a Song
song_select = (
    """
    SELECT song_id , artist_id 
    FROM songs s 
    JOIN artists a
    ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s
    """
)

# Query Lists

create_table_queries = [
    songplays_table_create,
    users_table_create,
    songs_table_create,
    artists_table_create,
    time_table_create
]

drop_table_queries = [
    songplays_table_drop,
    users_table_drop,
    songs_table_drop,
    artists_table_drop,
    time_table_drop
]