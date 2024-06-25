#Calculadora notas UOC


nota = float(input("¿Cuál es tu nota?\n"))
Total = float(input("¿Sobre cuánto?\n"))

nota_final = int((nota * 10)/Total)
print(f"Has sacado un {nota_final}")