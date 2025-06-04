##operacion con a b c
a = 5
b = 3 
c = a + b
print("c es igual a", a + b) 

print ("cuanto es 8 - 3?") 

respuesta = int(input("¿Cuánto es c - b? "))
if respuesta == c - b:
    print("¡Correcto!")
elif respuesta < c - b:
    print("Demasiado bajo.")
else:
    print("Demasiado alto.")

print("segundo ejercicio")

##informacion

print ("hola mi nombre es juan")
edad = 15 
peso = 56
estatura = 160
print("Tengo", edad, "años.")

## edad

pregunta2 = int(input("cual es tu edad?"))
if pregunta2 < 18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")

##for y while 

# Ejemplo de bucle for
print("Contando del 1 al 5 con for:")
for i in range(1, 6):
    print(i)

# Ejemplo de bucle while
print("Contando del 5 al 1 con while:")
contador = 5
while contador > 0:
    print(contador)
    contador -= 1