import datetime
from utilidad import utilidad01

saludo = ["Hola!\n", "le damos la bienvenida al examen de repuesta multiples\n", "Vamos a necesitar algunos datos.\n"]
for inicio in saludo:
    print(inicio)

fecha_inicial = datetime.datetime.now()  

nombre = str(input("Como te llamas: "))
apellido = str(input("Cuales son tus apellido: "))

respuestas = {}
    
respuestas[1] = utilidad01.mostrarPregunta("1.¿Cuantos dias tiene el año?", ["A) 365","B) 361","C) 366","D) 364"])
respuestas[2] = utilidad01.mostrarPregunta("2.¿Cuantos huesos tiene el ser humano?",["A) 210", "B) 209", "C) 206", "D) 211"])
respuestas[3] = utilidad01.mostrarPregunta("3.¿cuando fue la primera guerra mundial?",["A) 1910", "B) 1951", "C) 1945", "D) 1914"])
respuestas[4] = utilidad01.mostrarPregunta("4.¿cuantos segundos hay en un día?",["A) 91.100", "B) 86.400", "C) 82.600", "D) 86.300"])
respuestas[5] = utilidad01.mostrarPregunta("5.¿cuántos milímetros hay en un litro?",["A) 1010", "B) 950", "C) 1000", "D) 990"])

fecha_final = datetime.datetime.now()
tiempoRespuesta = fecha_final - fecha_inicial
utilidad01.validarRespuestas(nombre+apellido, len(respuestas), respuestas, tiempoRespuesta.total_seconds())







