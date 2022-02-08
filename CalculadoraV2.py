# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:47:46 2022

@author: dahmo
"""

calculadora=(int(input("Introduce que operación quieres hacer:\n \
1.Suma de dos números\n \
2.Resta de dos números\n \
3.Multiplicación de dos números\n \
4.División de dos números\n \
5.Módulo de dos números\n \
6.Cociente de dos números\n \
7.Exponente de dos números\n \
8.Calculadora de áreas de cuadrado para 'n' números pares\n \
9.Calculadora de áreas de círculos para 'n' números pares\n \
10.Salir\n     " )))
if calculadora == 1:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    resultado = n1 + n2
    print( "El resultado de la suma es", resultado )
    
elif calculadora == 2:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    resultado = n1 - n2
    print( "El resultado de la resta es", resultado )
elif calculadora == 3:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    resultado = n1 * n2
    print( "El resultado de la multiplicación  es", resultado )
elif calculadora == 4:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    while n2 == 0 :
        print( "El número introducido no puede ser igual a 0")
        n2=(float(input("Introduce otro número: ")))
    resultado = n1 / n2
    print( "El resultado de la división es:", resultado )
elif calculadora == 5:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    while n2 == 0 :
        print( "El número introducido no puede ser igual a 0")
        n2=(float(input("Introduce otro número: ")))
    resultado = n1 % n2
    print( "El módulo de la operación es:", resultado )
elif calculadora == 6:
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    while n2 == 0 :
        print( "El número introducido no puede ser igual a 0")
        n2=(float(input("Introduce otro número: ")))
    resultado = n1 // n2
    print( "El resultado de la operación es:", resultado )
elif calculadora == 7:
    n1=(int(input("Introduce un número: ")))
    n2=(int(input("Introduce otro número: ")))
    resultado = n1**n2
    print( "El resultado de la operación es", resultado )
elif calculadora == 8:
    x=1
    n1=(int(input("Introduce un número: ")))
    for i in range(1, n1):
        if x<=20 and i % 2==0:
            resultado = i**2
            print(f"El area del cuadrado {x} con lado {i} es igual a {resultado}")
            x=x+1    
elif calculadora == 9:
    x=1
    n1=(int(input("Introduce un número: ")))
    for i in range(1, n1):
        if x<=20 and i % 2==0:
            resultado = 3.1416*i**2
            print(f"El area del círculo {x} con radio {i} es igual a {resultado}")
            x=x+1        
elif calculadora == 10:
    print( "Adios")   
else:
    print("El número introducido no es ninguno de las funciones indicadas")