# #todo| hacer un diccionario en el que esten los nombres de los alumnos y sus notas y acceder a ellas
# #todo| en el que se puede añadir nuevos alumnos y borrar viejos

asignaturas = ["matematicas", "castellano", "ingles", "fisica y quimica"]
alumnos = {
    "ruben hontanilla fernandez":  {
            asignaturas[0]:4, asignaturas[1]:6, asignaturas[2]:9, asignaturas[3]:8
        }
}
notas = {}
while True:
    accion=input("\n-para acceder a las notas de un alumno escribe \"notas\"\n-para añadir un nuevo alumno escribe \"nuevo\"\n")
    match accion:
        case "notas":
            while True:
                solicitud = input("\n-escribe el nombre completo del alumno a consultar\n")
                if solicitud.lower() in alumnos:
                    print("\n")
                    notas = alumnos[solicitud.lower()]
                    for nombre, nota in notas.items():
                        print(f"en {nombre} tiene un", nota)
                else: 
                    break
        case "nuevo":
            while True:
                nombre = input("\n-introduce el nombre de el nuevo alumno (o salir)\n")
                if nombre == "salir":
                    break
                else:
                    for i in asignaturas:
                        notas[i] = input(f"\n-ingrese la nota que dicho alumno tiene en {i}\n")
                    alumnos[nombre] = notas
        case _:
            break