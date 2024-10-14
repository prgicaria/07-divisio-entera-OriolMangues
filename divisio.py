print('Aquest programa realitza una divisió')
a = float(input('Introdueix el divisor: '))
b = float(input('Introdueix el dividend: '))

# Comprobar si el divisor es zero
if a == 0:
    print("Error: No es pot dividir per zero.")
else:
    print('Divisió:', b, '/', a)
    print('Quocient:', b // a)  # División entera
    print('Residu:', b % a)     # Módulo para obtener el residuo
1
