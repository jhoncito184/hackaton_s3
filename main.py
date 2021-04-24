noteList = []
note = 0.0
maxLengthList = 5
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
print(f"El promedio es {str(sum(noteList) / maxLengthList)}")
print(f"El mayor valor es {max(noteList)}")
print(f"El menor valor es {min(noteList)}")