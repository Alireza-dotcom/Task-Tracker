import os

def load_stylesheet(app, path):
    if os.path.exists(path):
        with open(path, "r") as file:
            app.setStyleSheet(file.read())