class Persona:
    def __init__(self,nombre, apellido, edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad

if __name__ == '__main__':
    oPersona1=Persona('Jhon','Jordan', edad= 23)
    print(f'nombre:{oPersona1._nombre}')
    print(f'apellido;{oPersona1._apellido}')
    print(f'edad:{oPersona1._edad}')