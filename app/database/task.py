from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "summary": result[1],
            "description": result[2],
            "is_done": result[3]
        }
        out.append(result_dict)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)[0]


def update_by_id(task_id, task_body):
    task_tuple = (
        task_body.get("summary"),
        task_body.get("description"),
        task_body.get("is_done"),
        task_id
    )
    statement = """
        UPDATE task
        SET
            summary=?
            description=?
            is_done=?
        WHERE id=?
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (task_id, ))
    conn.commit()


def create(task_data):
    task_tuple = (
        task_data.get("summary"),
        task_data.get("description"),
    )
    statement = """
        INSERT INTO task (
            summary,
            description,
        ) VALUES (?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()