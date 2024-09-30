class Empleado_GGJ:
    def __init__(self, Rfc, Apellidos, Nombres):
        self.__Rfc = Rfc  
        self.__Apellidos = Apellidos
        self.__Nombres = Nombres
#Encapsulamiento
    def get_Rfc(self):
        return self.__Rfc

    def get_Apellidos(self):
        return self.__Apellidos

    def get_Nombres(self):
        return self.__Nombres

# Actualizador de atributos
    def set_Rfc(self, Rfc):
        self.__Rfc = Rfc

    def set_Apellidos(self, Apellidos):
        self.__Apellidos = Apellidos

    def set_Nombres(self, Nombres):  
        self.__Nombres = Nombres

#Informacion delempleado
    def mostrar_informacion(self):
        return f"Empleado: {self.__Rfc}, Apellidos: {self.__Apellidos}, Nombres: {self.__Nombres}"

class Empleadovendedor_GGJ(Empleado_GGJ):
    def __init__(self, Rfc, Apellidos, Nombres, monto_vendido, tasa_comision):
        super().__init__(Rfc, Apellidos, Nombres)  
        self.__monto_vendido = monto_vendido  
        self.__tasa_comision = tasa_comision  

    def get_monto_vendido(self):
        return self.__monto_vendido

    def get_tasa_comision(self):
        return self.__tasa_comision

    def mostrar_informacion_vendedor(self):
        return f"{self.mostrar_informacion()}, Monto vendido: {self.__monto_vendido}, Tasa de comisión: {self.__tasa_comision}"

    def calcular_ingresos(self):
        return self.__monto_vendido * self.__tasa_comision

    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        
        if self.__monto_vendido < 1000:
            bonificacion = 0  
        elif 1000 <= self.__monto_vendido <= 5000:
            bonificacion = ingresos * 0.05  
        else:
            bonificacion = ingresos * 0.10  

        return bonificacion
    def calcular_descuento(self):
        descuento = self.calcular_descuento

        if self.__ingresos_menores < 1000:
            descuento= 11

