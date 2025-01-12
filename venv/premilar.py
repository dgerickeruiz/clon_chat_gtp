import openai
import os

key = "aqui la key" #aqui hay que poner la key de OpenAI

openai.api_key = key

p1 = "¿cual son las alimentos mas saludables?"
p2 = "Crea una reeta con estos alimentos"
p3 = "¿cuantas calorias tiene esta recete?"
contexto = "responda lo mas conciso posible"
modelo = 'gpt-4o-mini'

mensajes = [
    {'role':'system', 'content':contexto},
    {'role':'user', 'content':p1}
]

respuesta = openai.chat.completions.create(
    messages = mensajes,
    model = modelo,
    temperature = 0.7
)

respuesta_gpt_1 = respuesta.choices[0].message.content
print(respuesta_gpt_1)
print()
print("*"*150)
print()

# Pregunta 2

mensajes = [
    {'role':'system', 'content':contexto},
    {'role':'user', 'content':p1},
    {'role':'assistant', 'content':respuesta_gpt_1},
    {'role':'user', 'content':p2}
]

respuesta = openai.chat.completions.create(
    messages = mensajes,
    model = modelo,
    temperature = 0.7
)

respuesta_gpt_2 = respuesta.choices[0].message.content
print(respuesta_gpt_2)
print()
print("*"*150)
print()

# Pregunta 3

mensajes = [
    {'role':'system', 'content':contexto},
    {'role':'user', 'content':p1},
    {'role':'assistant', 'content':respuesta_gpt_1},
    {'role':'user', 'content':p2},
    {'role':'assistant', 'content':respuesta_gpt_2},
    {'role':'user', 'content':p3}
]

respuesta = openai.chat.completions.create(
    messages = mensajes,
    model = modelo,
    temperature = 0.7
)

respuesta_gpt_3 = respuesta.choices[0].message.content
print(respuesta_gpt_3)
print()
print("*"*150)
print()
