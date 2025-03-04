# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str, creation_date, tags):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if self.tags.count(tag) < 1:
            self.tags.append(tag)

        else:
            return "La etiqueta ya existe"

    def __str__(self) -> str:
        return f"Date: {self.creation_date}\n{self.title}\n{self.text}"

class Notebook:
    def __init__(self,notes):
        self.notes:list[Note] =[]
