class Vehiculo:
    """
    Clase usada para crear objetos de tipo vehículo
    """

    def __init__(self, marca, modelo, color, placa, anio, tipo_de_puerta, combustible, kilometraje, caja_de_cambio, seguro, gama, chasis,
                 pais_de_origen, llanta_de_emergencia, numero_de_puertas):

        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._placa = placa
        self._anio = anio
        self._tipo_de_puerta = tipo_de_puerta
        self._combustible = combustible
        self._kilometraje = kilometraje
        self._caja_de_cambio = caja_de_cambio
        self._seguro = seguro
        self._gama = gama
        self._chasis = chasis
        self._pais_de_origen = pais_de_origen
        self._llanta_de_emergencia = llanta_de_emergencia
        self._numero_de_puertas = numero_de_puertas

    def __str__(self):
        return (
            f"Vehículo: marca: {self._marca}, modelo: {self._modelo}, color: {self._color}, placa: {self._placa}, "
            f"año: {self._anio}, tipo de puerta: {self._tipo_de_puerta}, combustible: {self._combustible}, "
            f"kilometraje: {self._kilometraje}, caja de cambio: {self._caja_de_cambio}, seguro: {self._seguro}, "
            f"gama: {self._gama}, chasis: {self._chasis}, país de origen: {self._pais_de_origen}, "
            f"llanta de emergencia: {self._llanta_de_emergencia}, número de puertas: {self._numero_de_puertas}"
        )

    def vender(self):
        print(f"El vehículo {self._marca} ha sido vendido exitosamente.")

    def acelerar(self):
        print(f"El vehículo {self._marca} está acelerando perfectamente.")

    def frenar(self):
        print(f"El vehículo {self._marca} está frenando perfectamente.")

    def girar(self, direccion):
        print(f"El vehículo {self._marca} está girando hacia la {direccion}.")

    def encender(self):
        print(f"El vehículo {self._marca} ha sido encendido perfectamente.")

    def apagar(self):
        print(f"El vehículo {self._marca} ha sido apagado.")

if __name__ == "__main__":
    objVehiculo1 = Vehiculo(
        "Toyota", "Corolla", "Rojo", "ABC1234", 2022,
        tipo_de_puerta="Convencional", combustible="Gasolina", kilometraje="15,000 km",
        caja_de_cambio="Automático", seguro="Responsabilidad civil", gama="Media",
        chasis="Compacto", pais_de_origen="Japón", llanta_de_emergencia="Sí", numero_de_puertas="4"
    )

    print(f"Marca: {objVehiculo1._marca}")
    print(objVehiculo1)

    objVehiculo1.vender()
    objVehiculo1.acelerar()
    objVehiculo1.frenar()
    objVehiculo1.girar("izquierda")
    objVehiculo1.encender()
    objVehiculo1.apagar()
