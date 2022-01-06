import random

def validarinput(param):
                while True:                        
                    x = input(param)
                    try:
                        x = int(x)
                        if x > 0:
                            return x
                        else:
                            print("Debes escribir un número positivo")
                            continue
                         
                    except ValueError:
                        print("Debes escribir un número positivo")
                        continue
                        
                    else:
                        break

def validardif(param):
                while True:

                    x = input(param)
                    try:
                        x = int(x)
                        if x > 0 and x <=10 :
                            return x
                        else:
                            print("Debes escribir un número entre 1 y 10")
                            continue
                         
                    except ValueError:
                        print("Debes escribir un número entre 1 y 10")
                        continue
                        
                    else:
                        break

def TiradorDeDados():
                numdados = validarinput("CANTIDAD DE DADOS: ")
                dificultad = validardif("DIFICULTAD: ")
                resultado = []
                exitos = []
                exitos_sobresalientes = []
                pifias = []


                for i in range (0 , numdados):
                    tirada = random.randint (1 , 10)
                    resultado.append(tirada)
                        
                    if tirada >= dificultad and tirada != 10:
                            exitos.append(tirada)

                    if tirada == 10:
                            exitos_sobresalientes.append(tirada)
                              
                    if tirada == 1:
                            if len(exitos_sobresalientes) > 0:
                                exitos_sobresalientes.pop()

                            elif len(exitos) > 0:
                                exitos.pop()
                            else:
                                pifias.append (i)
                                    

                print ("Resultado: ", resultado)
                if len(exitos) > 0 or len (exitos_sobresalientes) > 0 :
                    print ("N°exitos total: ", len(exitos) + len (exitos_sobresalientes) - len(pifias))
                else:
                    print ("N°exitos total: ", len(pifias) - ( 2 * len(pifias)))

                print ("////TIRADA TERMINADA////")
                
print("¡Bienvenido al tirador de dados de MdT!")
while True:
        TiradorDeDados()
