class Vehiculo:
    """
    Clase usada para crear objetos de tipo Vehiculo
    """
    def __init__(self, color, modelo, placa, valor, cilindraje, anio, tp_puertas,
                 combustible, kilometraje, cj_cambios, seguro, gama, chasis,
                 pais_origen, marca, llnt_emergencia, nm_puertas):
        self._color = color
        self._modelo = modelo
        self._placa = placa
        self._valor = valor
        self._cilindraje = cilindraje
        self._anio = anio
        self._tp_puertas=tp_puertas
        self._combustible=combustible
        self._kilometraje=kilometraje
        self._cj_cambios=cj_cambios
        self._seguro=seguro
        self._gama=gama
        self._chasis=chasis
        self._pais_origen=pais_origen
        self._marca=marca
        self._llnt_emergencia=llnt_emergencia
        self._nm_puertas=nm_puertas

    def __str__(self):
        return (f'Vehiculo [Marca: {self._marca}, Modelo: {self._modelo}, Color: {self._color}, Placa: {self._placa}, '
                f'Valor: {self._valor}, Cilindraje: {self._cilindraje}, Año: {self._anio}, Tipo de Puertas: {self._tp_puertas}, '
                f'Combustible: {self._combustible}, Kilometraje: {self._kilometraje}, Caja de Cambios: {self._cj_cambios}, '
                f'Seguro: {self._seguro}, Gama: {self._gama}, Chasis: {self._chasis}, País de Origen: {self._pais_origen}, '
                f'Llanta de Emergencia: {self._llnt_emergencia}, Número de Puertas: {self._nm_puertas}]')

if __name__ == '__main__':
    objVehiculo1 = Vehiculo(
        color='Negro',
        modelo='F150',
        placa='GRE2588',
        valor=25000,
        cilindraje=8000,
        anio=2018,
        tp_puertas='SUV',
        combustible='Gasolina',
        kilometraje=40000,
        cj_cambios='Automática',
        seguro='Sí',
        gama='Alta',
        chasis='XYZ1234567890',
        pais_origen='EE.UU.',
        marca='Chevrolet',
        llnt_emergencia='Sí',
        nm_puertas=4
    )
    print(objVehiculo1)