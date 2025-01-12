#
# Este prototipo va almacenando la conversacion, lo que produce
# promps mas complejos y costosos, tener cuidado con conversaciones
# extensas
#

import time

import openai
import os

key = "aqui la key" #aqui hay que poner la

openai.api_key = key

preguntas = list()
respuestas_gpt = list()
mensajes = list ()
#modelo = 'gpt-4o-mini'
modelo = 'gpt-4-turbo'

contexto = input("Sistema: Escribe un contexto: ")
if contexto == "":
    contexto = "responda lo mas conciso posible"

mensajes.append({'role':'system', 'content':contexto})

while True:
    pregunta_actual = input('Yo:')
    if pregunta_actual.lower() in ('exit','qqq','salir'):
        print('Bot: Nos vemos!')
        time.sleep(3)
        break
    if pregunta_actual == "":
        continue

    mensajes.append({'role':'user', 'content':pregunta_actual})
    respuestas = openai.chat.completions.create(
        messages=mensajes,
        model=modelo,
        temperature=0.7
        #max_tokens = 100
    )
    respuesta_actual = respuestas.choices[0].message.content
    print(f'\nBot: {respuesta_actual}')
    respuestas_gpt.append(respuesta_actual)
    mensajes.append({'role':'assistant', 'content':respuesta_actual})
    print()
    print("*" * 100)
    #print(respuestas)
    print("*" * 100)
    print()


# Para hacer ejecutable, hace en consola

# pip install Pyinstaler
# Pyinstaller --onefile clon_chatgpt.py

