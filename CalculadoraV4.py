# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:38:18 2021

@author: DiegoAlonsoHernando
"""
#FUNCIONES

# def pedirNum():
    
def sumar():
   n1=int(input("Introduce el primer número: "))
   n2=int(input("Introduce el segundo número: "))
   resultado=n1+n2
   print("El resultado de la suma es: ",resultado)

def restar():
   n1=int(input("Introduce el primer número: "))
   n2=int(input("Introduce el segundo número: "))
   resultado=n1-n2
   print("El resultado de la resta es: ",resultado)
   
def multiplicar():
   n1=int(input("Introduce el primer número: "))
   n2=int(input("Introduce el segundo número: "))
   resultado=n1*n2
   print("El resultado de la multiplicación es: ",resultado)
   
def dividir():
   n1=int(input("Introduce el primer número: "))
   n2=int(input("Introduce el segundo número: "))
   resultado=n1/n2
   print("El resultado de la multiplicación es: ",resultado)
   
def módulo():
    n1=(float(input("Introduce un número: ")))
    n2=(float(input("Introduce otro número: ")))
    while n2 == 0 :
        print( "El número introducido no puede ser igual a 0")
        n2=(float(input("Introduce otro número: ")))
    resultado = n1 % n2
    print( "El módulo de la operación es:", resultado )
    
def cociente():
   n1=(float(input("Introduce un número: ")))
   n2=(float(input("Introduce otro número: ")))
   while n2 == 0 :
       print( "El número introducido no puede ser igual a 0")
       n2=(float(input("Introduce otro número: ")))
   resultado = n1 // n2
   print( "El resultado de la operación es:", resultado )
   
def exponente(n1,n2):
   print(f"El resultado de {n1} elevado a {n2} es {n1**n2}")
   
def areaCuadrado():
    x=1
    n1=(int(input("Introduce un número: ")))
    for i in range(1, n1):
        if x<=20 and i % 2==0:
            resultado = i**2
            print(f"El area del cuadrado {x} con lado {i} es igual a {resultado}")
            x=x+1

def areaCirculo():
    x=1
    n1=(int(input("Introduce un número: ")))
    for i in range(1, n1):
        if x<=20 and i % 2==0:
            resultado = 3.1416*i**2
            print(f"El area del círculo {x} con radio {i} es igual a {resultado}")
            x=x+1
            
#CÓDIGO           
calculadora=0
while calculadora!=10:
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
    while calculadora < 1 or calculadora > 10:
        calculadora = int(input("Introduce una opción válida: "))
    if calculadora == 1:
        sumar()
    elif calculadora == 2:
        restar()
    elif calculadora == 3:
        multiplicar()
    elif calculadora == 4:
        dividir()
    elif calculadora == 5:
        módulo()
    elif calculadora == 6:
        cociente()
    elif calculadora == 7:
        n1=(int(input("Introduce un número: ")))
        n2=(int(input("Introduce otro número: ")))
        exponente(n1, n2)
    elif calculadora == 8:
        areaCuadrado()
    elif calculadora == 9:
        areaCirculo()
    elif calculadora == 10:
        print( "Adios")
        
    
    
    
    
    
    
    
    
    