class Vehiculo:
    def __init__(self, marca, modelo, color, placa, anio):
        self._color = color
        self._placa = placa
        self._anio = anio

    def __str__(self):
        return f'Vehiculo: {self.__dict__.__str__()}'
        return (f'Vehiculo[marca: {self._marca},modelo:{self._modelo}, color:{self._color},placa:{self._placa}, anio:{self._anio}]')

if __name__ == '__name__':
    objVehiculo1 = Vehiculo('Ford','F150', 'Negro','GREN2588', 2019)


    print(objVehiculo1)
