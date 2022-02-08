# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:23:19 2021

@author: DiegoAlonsoHernando
"""

#En esta función hago con un while que te pida un número hasta llegar a 5, y que si ese número está repetido o es mayor
#de 50 o es menor de 1, te salte un error y te haga repetir el número, después cada número introducido se añade a la lista
#listanumeros, por último te imprime los números que has elegido.
   
def pedirNum (x, listanumeros):
    while x != 5:
        numero = int(input("Por favor introduzca un número: "))
        if numero in listanumeros:
            print("NÚMERO MARCADO ANTERIORMENTE, ELIJA OTRO: ")
            numero = int(input("Por favor introduzca un número: "))
        while numero<1 or numero>50:
            print("ERROR, LOS NÚMEROS SELECCIONADOS TIENEN QUE ESTAR COMPRENDIDOS ENTRE EL 1 Y EL 50")
            numero = int(input("Por favor introduzca un número: "))
            if numero in listanumeros:
                print("NÚMERO MARCADO ANTERIORMENTE, ELIJA OTRO: ")
                numero = int(input("Por favor introduzca un número: "))
        listanumeros += [numero]
        x=x+1
        print()
    print(f"Los números elegidos son: {listanumeros}" )
    print()

#En esta función hago con un while que te pida un número hasta llegar a 2, y que si ese número está repetido o es mayor
#de 12 o es menor de 1, te salte un error y te haga repetir el número, después cada número introducido se añade a la lista
#listaestrellas, por último te imprime los números que has elegido.

def pedirEstr (v, listaestrellas):
    while v != 2: 
        estrella = int(input("Por favor introduzca una estrella: "))
        if estrella in listaestrellas:
            print("ESTRELLA MARCADA ANTERIORMENTE, ELIJA OTRA: ")
            estrella = int(input("Por favor introduzca una estrella: "))
        while estrella<1 or estrella>12:
            print("ERROR, LAS ESTRELLAS SELECCIONADAS TIENEN QUE ESTAR COMPRENDIDAS ENTRE EL 1 Y EL 12")
            estrella = int(input("Por favor introduzca una estrella: "))
            if estrella in listaestrellas:
                print("ESTRELLA MARCADA ANTERIORMENTE, ELIJA OTRA: ")
                estrella = int(input("Por favor introduzca una estrella: "))
        listaestrellas += [estrella]
        v=v+1
        print()
    print(f"Las estrellas elegidas son: {listaestrellas}" )
    print()

#Con esta función hago que si el número introducido es mayor de 10, es decir 
#tiene 2 digitos se cambie la x con unn espacio para utilizarlo en funciones más abajo

def x (x):
    if x<10:
        return "X"
    else:
        return " X"

#Con esta función comparo mediante dos for las listas de los números introducidos y la de los números
#del boleto, si ese número está en la lista, llamando a la función creada antes, hago que se tache, por último
#imprimo el boleto de los números con los números elegidos tachados    
def marcarNum (listanumeros):
    
    lista1=[1,10,19,28,37,46]
    lista2=[2,11,20,29,38,47]
    lista3=[3,12,21,30,39,48]
    lista4=[4,13,22,31,40,49]
    lista5=[5,14,23,32,41,50]
    lista6=[6,15,24,33,42]
    lista7=[7,16,25,34,43]
    lista8=[8,17,26,35,44]
    lista9=[9,18,27,36,45]
    
    for i in range(len(lista1)):
       for j in listanumeros:
            if lista1[i]==j:
             lista1[i]=x(j)
    for i in range(len(lista2)):
       for j in listanumeros:
            if lista2[i]==j:
             lista2[i]=x(j)
    for i in range(len(lista3)):
       for j in listanumeros:
            if lista3[i]==j:
             lista3[i]=x(j)
    for i in range(len(lista4)):
       for j in listanumeros:
            if lista4[i]==j:
             lista4[i]=x(j)
    for i in range(len(lista5)):
       for j in listanumeros:
            if lista5[i]==j:
             lista5[i]=x(j)
    for i in range(len(lista6)):
       for j in listanumeros:
            if lista6[i]==j:
             lista6[i]=x(j)
    for i in range(len(lista7)):
       for j in listanumeros:
            if lista7[i]==j:
             lista7[i]=x(j)
    for i in range(len(lista8)):
       for j in listanumeros:
            if lista8[i]==j:
             lista8[i]=x(j)
    for i in range(len(lista9)):
       for j in listanumeros:
            if lista9[i]==j:
             lista9[i]=x(j)
    print("----------------------------------")
    print("SUS NÚMEROS SELECCIONADOS SON: ")        
    print("|",*lista1,"|")
    print("|",*lista2,"|")
    print("|",*lista3,"|")
    print("|",*lista4,"|")
    print("|",*lista5,"|")
    print("|",*lista6,"   |")
    print("|",*lista7,"   |")
    print("|",*lista8,"   |")
    print("|",*lista9,"   |")
    print("----------------------------------")
    print()

#Con esta función comparo mediante dos for las listas de las estrellas introducidas y la de las estrellas
#del boleto, si esa estrella está en la lista, llamando a la unción creada antes, hago que se tache, por último
#imprimo el boleto de las estrellas con las estrellas elegidas tachadas    
    
def marcarEstr (listaestrellas): 
    lista10=[1,5,9]
    lista11=[2,6,10]
    lista12=[3,7,11]
    lista13=[4,8,12]
    
    for i in range(len(lista10)):
       for j in listaestrellas:
            if lista10[i]==j:
             lista10[i]=x(j)
    for i in range(len(lista11)):
       for j in listaestrellas:
            if lista11[i]==j:
             lista11[i]=x(j)
    for i in range(len(lista12)):
       for j in listaestrellas:
            if lista12[i]==j:
             lista12[i]=x(j)
    for i in range(len(lista13)):
       for j in listaestrellas:
            if lista13[i]==j:
             lista13[i]=x(j)
             
    print("----------------------------------")
    print("SUS ESTRELLAS SELECCIONADOS SON: ")        
    print("|",*lista10," |")
    print("|",*lista11,"|")
    print("|",*lista12,"|")
    print("|",*lista13,"|")
    print("----------------------------------")
    print() 
    
    
#Aquí creo dos listas vacías, para después ir añadiendo números en ella con el while, con la función random
#genero números aleatorios del 1 al 50, y en caso de que se repita, genera otro, una vez generado se añade a la lista

def generarGanadores (y, a, listaresnum, listaresest):
    import random
    
    while y!=5:
     resultadonum= random.randint(1,50)
     if resultadonum in listaresnum:
         resultadonum= random.randint(1,50)
     listaresnum += [resultadonum]
     y=y+1
     
    while a!=2:
     resultadoest= random.randint(1,12)
     if resultadoest in listaresest:
         resultadoest= random.randint(1,12)
     listaresest += [resultadoest]
     a=a+1
     
    print(f"Los números ganadores son {listaresnum} y las estrellas son {listaresest}")
    print()

#Aquí mediante dos for repaso las dos listas y las comparo, haciendo que los números que estén repetidos
#se añadan a otra lista que serán los números o estrellas que has acertado.    
def darPremios (listanumeros, listaestrellas, listaresnum, listaresest ):
    listanumgana=[]
    listaestgana=[]
    
    for i in listanumeros:
        for j in listaresnum:
            if i==j:
                listanumgana+=[i]
                print("----------------------------------")
                print(f"Tus números ganadores son: {listanumgana}")
                
    for i in listaestrellas:
        for j in listaresest:
            if i==j:
                listaestgana+=[i]
                print(f"Tus estrellas ganadoras son: {listaestgana}")
    print("----------------------------------")
#En esta parte añado a una variable el valor de la longitud de la lista de numeros acertados 
#y de estrellas acertadas, para despues mediante if y elif dar el premio final.

    totalnum=len(listanumgana)
    totalest=len(listaestgana)

    print(f"Total de números acertados: {totalnum}")
    print(f"Total de estrellas acertadas: {totalest}")

    if totalnum==5 and totalest==2:
        print("----------------------------------")
        print("5+2=15000000 €")
        print("----------------------------------")
    elif totalnum==5 and totalest==1:
        print("----------------------------------")
        print("5+1=3000000 €")
        print("----------------------------------")
    elif totalnum==5 and totalest==0:
        print("----------------------------------")
        print("5+0=1500000 €")
        print("----------------------------------")
    elif totalnum==4 and totalest==2:
        print("----------------------------------")
        print("4+2=800000 €")
        print("----------------------------------")
    elif totalnum==4 and totalest==1:
        print("----------------------------------")
        print("4+1=500000 €")
        print("----------------------------------")
    elif totalnum==4 and totalest==0:
        print("----------------------------------")
        print("4+0=350000 €")
        print("----------------------------------")
    elif totalnum==3 and totalest==2:
        print("----------------------------------")
        print("3+2=320000 €")
        print("----------------------------------")
    elif totalnum==3 and totalest==1:
        print("----------------------------------")
        print("3+1=300000 €")
        print("----------------------------------")
    elif totalnum==3 and totalest==0:
        print("----------------------------------")
        print("3+0=150000 €")
        print("----------------------------------")
    elif totalnum==2 and totalest==2:
        print("----------------------------------")
        print("2+2=50000 €")
        print("----------------------------------")
    elif totalnum==2 and totalest==1:
        print("----------------------------------")
        print("2+1=10000 €")
        print("----------------------------------")
    elif totalnum==2 and totalest==0:
        print("----------------------------------")
        print("2+0=60 €")
        print("----------------------------------")
    else:
        print("----------------------------------------")
        print("LO SENTIMOS, SU BOLETO NO TIENE PREMIO")
        print("----------------------------------------")