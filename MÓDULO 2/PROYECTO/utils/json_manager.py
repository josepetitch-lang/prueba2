import json

BOOKS_FILE = "../data/libros.json"
USERS_FILE = "../data/usuarios.json"

class JsonManager:
    def __init__(self, entity):
        self.entity = entity
        self.file_path = self._get_file_path()

    def _get_file_path(self):
        if self.entity == "libros":
            return BOOKS_FILE
        elif self.entity == "usuarios":
            return USERS_FILE
        else:
            raise ValueError("no")

    def read_json(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            
            return []

    def write_json(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)