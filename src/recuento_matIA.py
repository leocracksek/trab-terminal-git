instrumentos = ["pinza", "tijera", "pinza"]
esperadas = 2
observadas = 0
for instrumento in instrumentos:
    if instrumento == "pinza":
        observadas +=1

print("pinzas esperadas", esperadas)
print("pinzas observadas", observadas)

if observadas < esperadas:
    print("Faltan pinzas")
elif observadas > esperadas:
    print("Sobran pinzas")
else:
    print("Ni sobran ni faltan pinzas") 