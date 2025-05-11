import random
import time

print()
print("☠️"*50)
print("JUEGO DEL AHORCADO".center(50))
print("☠️"*50)

texto="\n Podes tener 6 intentos fallidos \n" \
"y dispones de solo 1 minuto para adivinar la palabra 🤓 ✏️"
for linea in texto.split("\n"):
 print(linea.center(60))

Categorias = ["Cuentos infantiles", "Peliculas clasicas", "Anatomia", "Colores"]

contenidos=[["Cenicienta","Caperucita", "Hansel y Gretel","Pinocho","El patito feo", "Blancanieves", "Los tres cerditos","Pulgarcito"],
["Psicosis", "El resplandor", "La vuelta al mundo en 80 dias", "La guerra de las galaxias", "El mago de oz", "Willi wonka", "El retrato de Dorian Grey"],
["corazon", "craneo","humero","tiroides", "ovarios","faringe","radio","higado","Bazo","Estomago","laringe", "vesicula biliar", "ileon","pancreas","humor vitreo"],
["rojo","amarillo","azul","naranja","verde","violeta","magenta","cian","gris","rosa","dorado","plateado","blanco","negro"]]

                #categorias y seleccion
print(f"\n Seleccione una categoria: \n")

for i, categoria in enumerate(Categorias,start=1):
    print(f"{i}.{categoria}")

opcion = int(input("\nIngrese la opcion 1-4: "))

if opcion >=1 and opcion <= len(Categorias):
  print(f"La Categoria seleccionada es {Categorias [opcion -1]}")

def categoria_seleccionada(opcion):
    p_elegida=random.choice(contenidos [opcion - 1])
    return p_elegida

#no mostrar!! es solo para saber la palabra que eligio el random
palabra_random=categoria_seleccionada (opcion)
print(palabra_random)

          #Comienzo del juego ingreso de letras y comparacion

intentos=0 #contador
intentos_restantes= 6
total_letras= ["_" ]*len(palabra_random)
letras_utilizadas=[ ]
palabra_oculta= palabra_random

while intentos_restantes > 0:
      letra=input("\nLetra ingresada: ").upper()
      print("Palabra: " + " ".join(total_letras))

      if letra in palabra_oculta.upper():
        for i, l in enumerate(palabra_oculta.upper()):
           if l == letra:
              total_letras[i]=letra
        print("☑️")
      else:
        print("🚩Error🚩")
        intentos= intentos +1
        print(f"Intentos:{intentos}")
        intentos_restantes=intentos_restantes -1
        print(f"Intentos restantes: {intentos_restantes}")
          #almacenamiento de las letras en la lista
      if letra in letras_utilizadas:
        continue
      letras_utilizadas.append(letra)
      print("Letras usadas: " + " ".join(letras_utilizadas))

      if intentos_restantes== 0:
       print(f"❌Partida perdida‼️☠️ ❌ \n La palabra oculta es {palabra_oculta} ")
       break