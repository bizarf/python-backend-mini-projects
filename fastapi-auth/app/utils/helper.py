from app.utils.database import get_db


# function to query the database for the username
def get_user(username):
    # database connection
    conn = get_db()
    # database cursor
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, username, password FROM users WHERE username = ?", (username,)
    )
    user = cursor.fetchone()
    # close the cursor and the connection
    cursor.close()
    conn.close()
    return user
