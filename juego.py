import random
import time

print()
print("☠️"*60)
print("JUEGO DEL AHORCADO".center(60))
print("☠️"*60)

texto="\n Podes tener 6 intentos fallidos \n" \
"y dispones de solo 1 minuto para adivinar la palabra 🤓 ✏️"
for linea in texto.split("\n"):
 print(linea.center(60))

Categorias = ["Cuentos infantiles", "Peliculas clasicas", "Anatomia", "Colores"]

contenidos=[["Cenicienta","Caperucita", "Hansel y Gretel","Pinocho","El patito feo", "Blancanieves", "Los tres cerditos","Pulgarcito"],
["Psicosis", "El resplandor", "La vuelta al mundo en 80 dias", "La guerra de las galaxias", "El mago de oz", "Willi wonka", "El retrato de Dorian Grey"],
["corazon", "craneo","humero","tiroides", "ovarios","faringe","radio","higado","Bazo","Estomago","laringe", "vesicula biliar"],
["rojo","amarillo","azul","naranja","verde","violeta","magenta","cian","gris","rosa","dorado","plateado","blanco","negro"]]

                #categorias y seleccion
print(f"\n Seleccione una categoria: \n")

for i, categoria in enumerate(Categorias,start=1):
    print(f"{i}.{categoria}")

#manejo de errores al ingreso de opciones
while True:
     try:
       opcion = int(input("\nIngrese la opcion 1-4: "))
       if opcion <=1 or opcion <=4:
         break
       else:
         print("Numero fuera de rango") 
     except ValueError:
       print("Por favor!, ingrese un numero valido")
       
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
intentos_maximos=6
intentos_restantes= intentos_maximos
total_letras= ["_" ]*len(palabra_random)
letras_utilizadas=[ ]
palabra_oculta= palabra_random
total_letras=["_" if c!=" " else " " for c in palabra_oculta]

#tiempo del juego
limite_tiempo= 60
tiempo_actual=time.time()
 

def iniciar_reloj():
 global inicio_t
 inicio_t= time.time()

def fin_tiempo():
  tiempo_actual=time.time()
  tiempo_transcurrido=tiempo_actual - inicio_t
  return tiempo_transcurrido== limite_tiempo

def intentos_terminados():
  return intentos_restantes<= 0
  

def jugar():
 global inicio_t,intentos_restantes,intentos
 iniciar_reloj()  
 tiempo_transcurrido= tiempo_actual - inicio_t
 while intentos_restantes > 0:
      print("Palabra: " + " ".join(total_letras))
      letra=input("\nLetra ingresada: ").upper()
      
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

      if fin_tiempo() or intentos_terminados():
       print(f"❌ 💀 Partida perdida ‼️ ☠️ ❌ \n La palabra oculta es {palabra_oculta} ")
       break
      if "_" not in total_letras:
        print("Palabra: " + " ".join(total_letras))
        print(f"PARTIDA GANADA 🎉🏆🥇🎉")
        break
jugar()

