import mysql.connector

def connect_db():
    db_name = "library_management"
    user = "root"
    password = "Wateva22@"
    host = "127.0.0.1" # or 127.0.0.1

    try: 
    # attempt to establish our connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )
        print("Connected Successfuly")
        return conn

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            conn.close()
connect_db()
