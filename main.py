import os
from pathlib import Path

from database import Database

cwd = Path.cwd()

databases = [file for file in cwd.iterdir() if file.is_file() and os.path.basename(file).endswith("db")]

if not databases:
    print("No databases found. Create now? (Y/n)")
    response = input()
    if "n" in response or "N" in response:
        print("Exiting")
        quit()
    else:
        print("Input the database name.")
        response = input().strip()
        db_file = Path(f"{response}.db")
        db_file.touch()
else:
    db_file = databases[0]

db = Database(db_file)
print("Starting database " + db.name)