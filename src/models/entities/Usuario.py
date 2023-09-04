
from utils.DateFormat import DateFormat

class Usuario():

    def __init__(self, id, ci=None, nombre=None, primer_ap=None, segundo_ap=None, fecha_nac=None) -> None:
        self.id = id
        self.ci = ci
        self.nombre = nombre
        self.primer_ap = primer_ap
        self.segundo_ap = segundo_ap
        self.fecha_nac = fecha_nac

    def to_JSON(self):
        return {
            "id": self.id,
            "ci": self.ci,
            "nombre": self.nombre,
            "primer_ap": self.primer_ap,
            "segundo_ap": self.segundo_ap,
            "fecha_nac": DateFormat.convert_date(self.fecha_nac)
        }
