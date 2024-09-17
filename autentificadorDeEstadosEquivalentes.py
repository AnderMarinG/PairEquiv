#Versión 1.1
#cambios:
#-Se cambió el segundo to string, para que queden en parentesis
# -Se creaban mas estados del que se pedian, eso se resolvió.
# -Se imprimen todos ahora en una misma linea

#clase de las parejas.
class pareja:
    def __init__(self,part1 ,part2):
        self.estado1 = part1
        self.estado2 = part2
        self.marca = False
    
    def toString(self):
        resultado = str(self.estado1) + " " + str(self.estado2) + " " + str(self.marca)
        return resultado
    
    def toString2(self):
        resultado = "(" + str(self.estado1) + " ≈ " + str(self.estado2) + ")"
        return resultado
    
    def getMarca(self):
        return self.marca
    
    def setMarcaTrue(self):
        self.marca = True
    
    def getEstado1(self):
        return self.estado1        
    
    def getEstado2(self):
        return self.estado2

def convertir(persona, arrayTransc, posLetra):
    for i in arrayTransc:
        transicionesSeparadas = i.split(" ")
        if (int(persona.getEstado1()) == int(transicionesSeparadas[0])):
            num1 = int(transicionesSeparadas[posLetra])
        if (int(persona.getEstado2()) == int(transicionesSeparadas[0])):
            num2 = int(transicionesSeparadas[posLetra])
    if(num1 < num2): 
        return [num1, num2]
    else:
        return [num2, num1]

def comparacion(pareja, arrayConvertido):

    if(int(arrayConvertido[0]) == int(pareja.getEstado1()) and int(arrayConvertido[1]) == int(pareja.getEstado2())):
        if(pareja.getMarca()):
            return True
    else: 
        return False
            
#Main.
if __name__ == '__main__': 
    #entradas
    
    print("Digite el numero de casos: ")
    casos = int(input())
    if(casos <= 0): 
        raise ValueError(f'El numero de casos tiene que ser mayor que 0.')
    
    arrayParejasCasos = []
    
    controlTotal = 1
    while(controlTotal <= casos):
        print("caso n° " + str(controlTotal) )
        
        print("Digite el número de estados del lenguaje: ")
        estados = int(input())-1
        if(estados <= 0):
            raise ValueError(f'El numero de estados tiene que ser mayor que 0.')

        print("Digite el alfabeto del lenguaje, en una linea, separados por espacio: ")
        alfabeto = input()
        arrayAlfabeto = alfabeto.split(" ")
        
        print("Digite los estados finales, separados por espacio: ")
        estadoFinal = input()
        estadosFinalesArray= estadoFinal.split(" ")
        for i in estadosFinalesArray: 
            verificacion = int(i)
            if(verificacion < 1 or verificacion > estados):
                raise ValueError(f'Los estados finales tienen que estar entre los casos.')
   
        print("Digite las lineas de transiciones, cada caso entre espacios")
        arrayTransiciones = []
        controlTrans = 0
        while(controlTrans<= estados):
            print("Linea n°" + str(controlTrans+1))
            arrayTransiciones.append(input())
            controlTrans = controlTrans+1
    
        #creación de parejas con POO
        arrayParejas = []
        controlPar = 0
        while(controlPar <= estados):
            controlParj= controlPar+1
            while(controlParj <= estados):
                temp = pareja(controlPar,controlParj)
                arrayParejas.append(temp)
                controlParj = controlParj+1
            controlPar= controlPar+1
        
        #primera verificación, si una pareja si es final y la otra no
        for i in arrayParejas:
            estadoUnoFinal = False
            estadoDosFinal = False
            for j in estadosFinalesArray:
                if(int(j) == int(i.getEstado1())):
                    estadoUnoFinal = True
                if(int(j) == int(i.getEstado2())):
                    estadoDosFinal = True
            if(estadoUnoFinal != estadoDosFinal):
                i.setMarcaTrue()
                
        #verificaciones de los estados:
        #simula un do-while
        #guarda primero una version de las marcas anteriores sin cambio
        #Luego, hace los cambios
        #Compara, si existen cambios, vuelve a hacer el ciclo, si no hay cambios, para
        estadoComparaciones = True
        while(estadoComparaciones):
            marcaAntes = []
            controlParejas = 0
            while(controlParejas < len(arrayParejas)):
                controlLetras = 1
                marcaAntes.append(arrayParejas[controlParejas].getMarca())
                while(controlLetras < len(arrayAlfabeto)+1):
                    if(arrayParejas[controlParejas].getMarca() == True):
                        break
                    convertido = convertir(arrayParejas[controlParejas], arrayTransiciones, controlLetras)
                    controlParejas2 = 0
                    while(controlParejas2 < len(arrayParejas)):
                        if(controlParejas != controlParejas2):
                            aprobacion = comparacion(arrayParejas[controlParejas2], convertido)
                            if(aprobacion == True):
                                arrayParejas[controlParejas].setMarcaTrue()
                        controlParejas2 = controlParejas2 +1
                    controlLetras = controlLetras +1        
                controlParejas = controlParejas +1  
            #controlador de volver a hacer el ciclo
            estadoComparaciones = False
            controlComparacion = 0
            while(controlComparacion < len(arrayParejas)):
                if(arrayParejas[controlComparacion].getMarca() != bool(marcaAntes[controlComparacion])):
                    estadoComparaciones = True
                    break
                controlComparacion = controlComparacion+1
        arrayParejasCasos.append(arrayParejas)
        controlTotal = controlTotal+1
    
    controlFinal = 0
    while(controlFinal < len(arrayParejasCasos)):
        print("Caso n°" + str(controlFinal+1))
        resultado = ""
        for z in arrayParejasCasos[controlFinal]:
            if(z.getMarca() == False):
                resultado = resultado + str(z.toString2()) + " "
        print(resultado)
        controlFinal = controlFinal+1