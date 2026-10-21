# Creo la lista con los registros sinteticos de instrumentos
instrumentos = ["pinza", "tijera", "pinza"]
#Fijo el numero de pinzas esperadas y empiezo el recuento en 0
esperadas = 2
observadas = 0
#Recorro la lista con un bucle for
for instrumento in instrumentos:
    #Compruebo si el elemento actual es una pinza
    if instrumento == "pinza":
        #Si es una pinza, suma una al contador
        observadas +=1

#Muestro lo obtenido
print("pinzas esperadas", esperadas)
print("pinzas observadas", observadas)

#Uso if, elif y else para decidir el resultado final
if observadas < esperadas:
    print("Faltan pinzas")
elif observadas > esperadas:
    print("Sobran pinzas")
else:
    print("Ni sobran ni faltan pinzas") 