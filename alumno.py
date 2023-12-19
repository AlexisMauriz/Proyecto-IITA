class Curso:
    def __init__(self, PythonI, PythonII, MarketingDigital, Robotica, Contacto):
        self.PythonI = PythonI
        self.PythonII = PythonII
        self.MarketingDigital = MarketingDigital
        self.Robotica = Robotica
        self.Contacto = Contacto
        self.cursos = []

    def to_dict(self):
        return vars(self)

class Alumno:
    def __init__(self, Nombre, Apellido, Edad, DNI, Contacto):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.DNI = DNI
        self.Contacto = Contacto
        self.cursos = []

    def to_dict(self):
        return vars(self)

  