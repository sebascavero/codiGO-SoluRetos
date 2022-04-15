n_personas = int(input("Ingrese el número de personas que desea registrar: "))
lista_presonas=[]

for i in range (n_personas):
    nombre = input("Ingrese el nombre de la persona: ")
    DNI = int(input("Ingrese el DNI de la persona: "))
    fecha_naci = input("Ingrese la fecha de nacimiento de la persona con el formato dd/mm/aaaa: ")
    persona ={
        "nombre": nombre,
        "dni": DNI,
        "fecha_naci": fecha_naci
    }
    lista_presonas.append(persona)

print(lista_presonas)