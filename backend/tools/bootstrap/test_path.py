from pathlib import Path

from backend import app

filename = "location.csv"
folder_to_save_file = Path(app.config["UPLOAD_FOLDER"])
path_to_save_file = folder_to_save_file / filename

print(path_to_save_file.resolve())
print(Path.cwd())
