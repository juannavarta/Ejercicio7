import csv
from classViajero import ViajeroFrecuente
if __name__ == "__main__":
    viajeros = []
    archivo = open('C://Users//csv//Viajeros.csv', 'r')
    reader = csv.reader(archivo, delimiter=";")
    for fila in reader:
        num = int(fila[0])
        dni = fila[1]
        nom = fila[2]
        ape = fila[3]
        millas = int(fila[4])
        viaje = ViajeroFrecuente(num, dni, nom, ape, millas)
        viajeros.append(viaje)
    archivo.close()
    i=0
    while i==0:
        print("Menu")
        print("1. Consultar Millas")
        print("2. Acumular Millas")
        print("3. Canjear Millas")
        print("4. Determinar viajero/s con mayor cantidad de millas acumuladas")
        print("5. Lo mismo que el 2, otro metodo")
        print("6. Lo mismo que el 3, otro metodo")
        print("7. Comparar millas ingresadas por teclado con las de un viajero, por derecha e izquierda")
        print("8. Lo mismo que el 5, pero conmutativo")
        print("9. Lo mismo que el 6, pero conmutativo")
        print("0. Cerrar")
        opcion = int(input())
        if opcion==0:
            exit()
        elif opcion==1:
            j=0
            numV = int(input("Ingrese numero de viajero a consultar: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                print("El viajero con numero {} tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))
        elif opcion==2:
            j=0
            numV = int(input("Ingrese numero de viajero a acumular millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a acumular: "))
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].acumularMillas(mil)))
        elif opcion==3:
            j=0
            numV = int(input("Ingrese numero de viajero a canjear millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a canjear: "))
                if mil <= viajeros[j].getMillas():
                    print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].canjearMillas(mil)))
                else:
                    print("La cantidad de millas seleccionadas no alcanzan para realizar el canje")
            print(max.getMillas)
        elif opcion==4:
            maxViajero = max(viajeros)
            print(f"El viajero con mas millas acumuladas es {maxViajero.getApellido()}, {maxViajero.getNombre()}")
        elif opcion==5:
            j=0
            numV = int(input("Ingrese numero de viajero a acumular millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a acumular: "))
                viajeros[j] = viajeros[j] + mil
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))
        elif opcion==6:
            j=0
            numV = int(input("Ingrese numero de viajero a canjear millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a canjear: "))
                viajeros[j] = viajeros[j] - mil
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))      
        elif opcion==7:
            j=0
            numV = int(input("Ingrese numero de viajero a comparar millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a comparar: "))
                if mil==viajeros[j] or viajeros[j]==mil:
                    print("El viajero con numero {} si tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))
                else:
                    print(f"No posee {mil} millas")
        elif opcion==8:
            j=0
            numV = int(input("Ingrese numero de viajero a acumular millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a acumular: "))
                viajeros[j] = mil + viajeros[j]
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))
        elif opcion==9:
            j=0
            numV = int(input("Ingrese numero de viajero a canjear millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a canjear: "))
                viajeros[j] = mil - viajeros[j]
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].getMillas()))
        else:
            print("Opción Inválida")