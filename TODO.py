import argparse
import sqlite3


parser = argparse.ArgumentParser(description="TODO Application")

parser.add_argument("--install", action="store_true", help="Initialize the database and create tables")
parser.add_argument("--add", type=str, help="Add a new TODO item")
parser.add_argument("--list", action="store_true", help="List all TODO items")
parser.add_argument("--done", type=int, help="Mark a TODO item as completed by its ID")

args = parser.parse_args()


if args.install:
    print("[DEBUG] Initializing the database...")
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor() 
    cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, is_done INTEGER DEFAULT 0)")
    connection.commit()
    connection.close()
    print("[DEBUG] Database file and table created successfully.")


if args.add:
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (title) VALUES(?)", (args.add,))
    connection.commit()
    connection.close()
    print("[DEBUG] Task added to the database successfully.")


if args.list:
    print("[DEBUG] Listing all tasks from the database...")
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, is_done FROM todos")
    tasks = cursor.fetchall()
    
    for task in tasks:
        if task[2] == 1:
            status = "[X]"
        else:
            status = "[ ]"
        # Teraz drukujemy z flagą statusu
        print(f"{task[0]}. {status} {task[1]}")

    connection.close()


if args.done:
    print(f"[DEBUG] Marking task ID {args.done} as completed...")
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE todos SET is_done = 1 WHERE id = ?", (args.done,))
    connection.commit()

    connection.close()
    print("[DEBUG] Task marked as completed successfully.")