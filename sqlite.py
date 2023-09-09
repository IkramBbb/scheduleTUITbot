import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, name TEXT, course TEXT, faculty TEXT, language TEXT)"
    )

    db.commit()


async def create_profile(user_id, state):
    user = cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)
    ).fetchone()
    if not user:
        async with state.proxy() as data:
            cur.execute(
                "INSERT INTO profile VALUES(?, ?, ?, ?, ?)",
                (user_id, data['name'], data['course'], data['faculty'], data['language']))
            db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET name = '{}', course = '{}', faculty = '{}', language = '{}' WHERE user_id == '{}'".format(
            data['name'], data['course'], data['faculty'], data['language'], user_id))
        db.commit()


async def is_authorized(user_id):
    return cur.execute(
        "SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)
    ).fetchone()


async def select_data(user_id):
    data = cur.execute("SELECT language, faculty FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    return data

