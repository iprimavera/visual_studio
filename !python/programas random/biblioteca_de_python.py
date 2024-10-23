accion = input("""que deseas consultar?
* tipos de comentarios extension (comentarios)
* comandos de calculo (calculos)
""")
match accion:
    case "comentarios":
        print("""\
- # comentario verde
- #! comentario rojo
- #? comentario azul
- #// comentario tachado
- #todo comentario amarillo 
- #* comentario verde clarito
""")
    case "calculos":
        pass #todo acabar esto
    case _:
        print("esa no es una opcion valida")