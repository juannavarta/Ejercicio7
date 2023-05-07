class ViajeroFrecuente:
    __numViajero = 0
    __dni = ""
    __nom = ""
    __ape = ""
    __millasAc = 0
    def __init__(self, num, dni, nom, ape, mil):
        self.__numViajero = num
        self.__dni = dni
        self.__nom = nom
        self.__ape = ape
        self.__millasAc = mil
    def getMillas(self):
        return self.__millasAc
    def acumularMillas(self, millas):
        self.__millasAc = self.__millasAc + millas
        return self.__millasAc
    def canjearMillas(self, millasCanje):
        self.__millasAc = self.__millasAc - millasCanje
        return self.__millasAc
    def getNumero(self):
        return self.__numViajero
    def __gt__(self, otroViajero):
        return self.__millasAc > otroViajero.getMillas()
    def getNombre(self):
        return self.__nom
    def getApellido(self):
        return self.__ape
    def __add__(self, num):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nom, self.__ape, self.__millasAc+num)
    def __radd__(self, num):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nom, self.__ape, self.__millasAc+num)
    def __sub__(self, num):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nom, self.__ape, self.__millasAc-num)
    def __rsub__(self, num):
        return ViajeroFrecuente(self.__numViajero, self.__dni, self.__nom, self.__ape, self.__millasAc-num)
    def __eq__(self, valor: object) -> bool:
        return self.__millasAc == valor