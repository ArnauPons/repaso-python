print("hola mundo")
#soy un comentario super guay y frutifantástico



 #Variables

texto= "Hola me llamo "
nombre= "pepe antonio, mido"
altura= "179 y nací en"
año= "2006"

print (f"{texto} {nombre} {altura} {str(año)}")
print (texto + " - " + nombre+ " - " + altura + " - " + str(año))

#Entrada
sitioweb = input("¿cual es tu página web: ")
print( "el siitio web del usuario es: " + sitioweb)
altura = 179
"""
altura = int (input ("¿Cual es tu altura?:"))

if altura >= 170:
    print("eres una persona alta!!!")

else:
    print("Eres BAJITO!!")
"""
#funciones

def mostraraltura():

    altura = int (input ("¿Cual es tu altura?:"))

if altura >= 170:
    print("eres una persona alta!!!")

else:
    print("Eres BAJITO!!")