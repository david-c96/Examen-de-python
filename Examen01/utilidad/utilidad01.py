import datetime
import math
def mostrarPregunta(pregunta:str,respuesta:dict):
    respuesta = respuesta
    print(pregunta)
    for respuestaPorLinea in respuesta:
        print(respuestaPorLinea)
    respuestaSeleccionada = input("Escriba su respuesta: ").lower()
    #Validamos la respuesta que sea correcta
    if("a,b,c,d".find(respuestaSeleccionada) >= 0 ):
        #guardarRespuesta(numeroPregunta,respuestaSeleccionada)
        return respuestaSeleccionada;
    else:
        print("Por favor escoja una respuesta valida")
        mostrarPregunta(pregunta, respuesta)

def validarRespuestas(respuestas:dict, cantidadPregunta1:int, tiempoRespuesta,nombreCompleto:str):
    print("\n")
    print("Fecha del examen:", datetime.datetime.now().strftime("%x"))
    print(f"Nombre Completo: {nombreCompleto} ")
    print(f"Cantidad de preguntas: {cantidadPregunta1}")
    print("Tiempo a responder: 2 min")
    print(f"Tiempo en que se demoro en responder: {round(tiempoRespuesta/60, 2)} min")
    respuestasCorrectas = {1:"a", 2:"c", 3:"d", 4:"b", 5:"c"}
    cantidadRespuestasCorrectas = 0
    for i in respuestas:
        if(respuestasCorrectas.get(i) == respuestas.get(i)):
             cantidadRespuestasCorrectas = cantidadRespuestasCorrectas + 1
           
    print(f"Resultado final: Respondio {cantidadRespuestasCorrectas} preguntas correctas de {cantidadPregunta1} preguntas" ) 

    resultado = (100/cantidadPregunta1)*cantidadRespuestasCorrectas
    print(f"Nota final: {resultado}")                                               