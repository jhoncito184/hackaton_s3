noteList = []
note = 0.0
maxLengthList = 5
nombre = input("Cual es tu nombre ?\n")

while len(noteList) < maxLengthList:
    try:
        note = int(input("Ingresa una nota: "))
        if note <= 20:
            noteList.append(note)
        else:
            print('La nota debe ser menor o igual a 20, vuelve a ingresar')
    except (TypeError, ValueError) as e:
        print(f'El valor ingresado no es un numero, vuelve a ingresar el valor')
    except Exception as e:
        print(e.__class__.__name__)
        print(f'Ocurrio un problema: {e}')

print('\n')
print(noteList)
print(f"El promedio de {nombre} es de {str(sum(noteList) / maxLengthList)}")
print(f"La nota mayor de {nombre} es de {max(noteList)}")
print(f"La menor nota de {nombre} es de {min(noteList)}")