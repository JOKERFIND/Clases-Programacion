#def suma(a, b):
#    return a+b

#def sumap(a, b):#XXXXX
#    print(a+b)

#entry point
#if __name__ =="__main__":
#   print (suma(2, 2))
#   sumap(3, 3)

#____tipado dinamico____

#x=10
#print(x,"addr:",id(x))
#x="hola"
#print(x,"addr:",id(x))

#y=10
#print(y,"addr:",id(y))

#z="holA"
#print(z,"addr:",id(z))

#x=1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))
#x=x+1
#print(x, ":", id(x))

#print(x:=10)


#def suma1(a,b):
#    return a+b

#def suma2(a:int,b:int)->int:
#    return a+b

#print(suma1(2,2))
#print(suma2(3,3))
#analisis estatico
#pip install mypy

#*Ejercicios*

#def nombre(saludo:str, nmbr:str)->str:
#    print (saludo, nmbr)
#    return nombre

#nmbr="Jose"
#saludo="Buenos dias"
#nombre(saludo, nmbr)

#def sald(sl:str, nm:str, sl1:str, edad:str, sl2:str)->str:
#    print(sl, nm, sl1, edad, sl2)
#    return sald

#sl="Hola"
#sl1="tienes"
#sl2="años"
#nm=input("Ingrese su nombre: ")
#edad=input("Ingrese su edad: ")

#sald(sl, nm, sl1, edad, sl2)

#def edd(s:str, nb:str, s1:str, edd1:int, s2:str)->str:
#    print(f"{s} '{nb}' {s1} {edd1} {s2}")
#    return edd

#s="Hola"
#s1="tienes"
#s2="años"
#nb=input("Ingrese su nombre: ")
#añoact=int(input("Ingrese el año actual: "))
#añonc=int(input("Ingrese el año de nacimiento: "))
#r=añoact-añonc
#edd(s,nb,s1,r,s2)

#s="Hola"
#s1="tienes"
#s2="años"
#nb=input("Ingrese su nombre: ")
#añoact=input("Ingrese el año actual")
#añonc=input("Ingrese el año de nacimiento")





#def cuadrado(n: int)->int|float: return n*n

#def suma(a:int|str,b:int|str)->int|str: return a+b

#print(suma(1, 1))
#print(suma("Hola", "mundo"))

##print(suma(1, "hola"))
##print(cuadrado(2))

####---31 de agosto---####

#n1=10
#msg="Hola"

#print(n1, msg)
#print(str(n1)+msg)
##fstrings
#print(f"{n1} {msg}")
#print(f"\"{n1}\" \"{msg}\"")

#Hacer una funcion que reciba el nombre de una persona el año de nacimiento y el año
#de nacimiento y el año actual retornando el mensaje
#"Hola <nombre>, tienes <edad> años"


#def presentacion(nombre:str, anc:int, anac:int)->str:
# r=anac-anc
# return f"Hola {nombre}, tienes {r} años"
#
#def presentacion2(nombre:str, anc:int, anac:int)->str:
# return f"Hola {nombre}, tienes {anac-anc} años"
#
#def calcular_edad(anc:int, anac:int)->str:
#    return anac-anc
#
#def presentacion3(nombre:str, anc:int, anac:int)->str:
# return f"Hola {nombre}, tienes {calcular_edad(anc, anac)} años"
#
#if __name__=="__main__":
#    print(presentacion("Ruben", 2002, 2022))
#    print(presentacion("Jose", 1999, 2022))
#    res=presentacion2("Antonio", 1974, 2022)
#    print(res)
#    print(presentacion("Alejandro", 1992, 2022))
#
##listas
#
#alumnos=["Hugo", "Paco", "Luis", "Lupita"]
#print(f"Alumnos: {alumnos}")
#
#for i in range(len(alumnos)):
# print(f"Alumnos:{alumnos[i]}")
#
##tuplas
#alumnos=("Hugo", "Paco", "Luis", "Lupita")
#print(f"Alumnos: {alumnos}")
#
#for i in range(len(alumnos)):
# print(f"Alumno {i+1}:{alumnos[i]}")
#
##sets
#alumnos={"Hugo", "Paco", "Luis", "Lupita"}
#print(f"Alumnos: {alumnos}")

#diccionarios
#alumnos={"nombre": "Hugo", "Material":10, "Material2":5}
#print(f"Alumnos: {alumnos}")
#print(f"Alumnos: {alumnos['nombre']}")
#
#nm_list=[1,2,3,3,4,2,2,1,4,3,7,4,6,9,7,6,2,2,5,3,2]
#nm_set={1,2,3,3,4,2,2,1,4,3,7,4,6,9,7,6,2,2,5,3,2}
#print(nm_list)
#print(nm_set)


#e=["Nombre", "Est Dat", "Prog Func", "Ingles"]
#alumnos=["Hugo", "Paco", "Luis", "Lupita"]
#
#m_e_d=[9,7,9,8]
#m_p_f=[10,8,7,9]
#m_i=[6,9,7,10]
#
#print(f"{e[0]:^10}{e[1]:^10}{e[2]:^10}{e[3]:^10}")
#for i in range(len(alumnos)):
#    print(f"{alumnos[i]:^10}{m_e_d[i]:^10}{m_p_f[i]:^10}{m_i[i]:^10}")

#print(f"{e[0]:^10}{e[1]:^10}{e[2]:^10}{e[3]:^10}")
#for i in range(len(alumnos)):
#    print(f"{alumnos[i]:<10}{m_e_d[i]:^10}{m_p_f[i]:^10}{m_i[i]:^10}")

#ancho=15
#print(f"{e[0]:^{ancho}}{e[1]:^10}{e[2]:^10}{e[3]:^10}")
#for i in range(len(alumnos)):
#    print(f"{alumnos[i]:^10}{m_e_d[i]:^10}{m_p_f[i]:^10}{m_i[i]:^10}")
#
#e=["Nombre", "Est Dat", "Prog Func", "Ingles"]
#alumnos=["Hugo", "Paco", "Luis", "Lupita"]
#m_e_d=[9,7,9,8]
#m_p_f=[10,8,7,9]
#m_i=[6,9,7,10]
#
#def reporte(fmt: int):
#    print(f"{e[0]:^{fmt}}{e[1]:^{fmt}}{e[2]:^{fmt}}{e[3]:^{fmt}}")
#    for i in range(len(alumnos)):
#     print(f"{alumnos[i]:-^{fmt}}{m_e_d[i]:-^{fmt}}{m_p_f[i]:-^{fmt}}{m_i[i]:-^{fmt}}")
#
#if __name__=="__main__":
#    reporte(12)

#numerobig=123435643213435324325432435
#print(f"numero: {numerobig:,d}")
##fijar cantidad de decimales
#numeropi=3.141592678547
#print(f"numero pi: {numeropi:.3f}")
##notacion cientifica
#print(f"numero pi: {numeropi:e}")
#print(f"numero pi: {numeropi:.2e}")
##porcentaje
#numeroporciento=0.2385627465
#print(f"Porcentaje: {numeroporciento:%}")
#print(f"Porcentaje redondeado: {numeroporciento:.2%}")
##numeros binarios
#print(f"{732:b}")
##Unicodes
#print(f"{35:c}{69:c}")
##hexadecimal
#print(f"{255:x}")
##octal
#print(f"{255:o}")

"""
Escribe una funcion que genere una tabla de multiplicar
"""
#def resultado(a:int, b:int)->int: return a*b
#def tablas(m:int, q:int, fmt:int):
#    for i in range(1, m+1):
#        tabla(q, i, fmt)
#        print("")
#def tabla(c:int, d:int, fmt:int):
# for i in range(1, c+1):
#     print(F"{d:^{fmt}}*{i:^{fmt}}= {resultado(d, i):<{fmt}}")
#     
#
#if __name__=="__main__":    
#    tablas(3, 4, 6)


#lista1=[1,2,3,4,5,6]
#print(lista1)
#lista2=[1, 3.1416, "a", True, [4,5,6],(2,8,1),(8,"a",5.4)]
#print(lista2)
#
#len(lista1)
#print(lista2[6])
#
#lista_cal=[]
#print(lista_cal)
#lista_cal.append(5)
#print(lista_cal)
#lista_cal.append(8)
#print(lista_cal)
#
##lista_nm=[]
##lista_nm.extend([1,2,3,4,5,6,7,8,9,10])
##print(lista_nm)
#
##rellenar una lista con los numeros naturales del 1 al 10
#
#lista_nm2=[]
#n=0
#for i in range(1,11):
#    n=n+1
#    lista_nm2.append(n)
#
#print(lista_nm2)
#
#print(lista_nm2[-2])

#slices(rebanadas)

#lista1=[1,2,3,4,5,6,7,8,9,10]
#print(lista1)
#print(lista1[:])
#print(lista1[0:10])
#print(lista1[int(len(lista1)/2):])
#
#print(lista1[:int(len(lista1)/2)])
#print(lista1[0:-1])
#print(lista1[3:7])
#print(lista1[-7:-3])
#
#from pickle import LIST
#
#
#lista1=[1,"dos", 3, "cuatro"]
##print(lista1)
##lista1[1]=2
#lista2=lista1
#print(f"Lista 1: {lista1}")
#print(f"Lista 2: {lista2}")
#print("---------------------------")
#lista2[1]=2
#print(f"Direccion:{id(lista1)} Lista 1: {lista1}")
#print(f"Direccion:{id(lista1)} Lista 2: {lista2}")
#print("---------------------------")
#print("forma correcta")
#lista1=[1,"dos", 3, "cuatro"]
#lista2=lista1[:]
#print(f"Direccion:{id(lista1)} Lista 1: {lista1}")
#print(f"Direccion:{id(lista1)} Lista 2: {lista2}")
#print("-------")
#lista2[1]=2
#lista2[3]=4
#print(f"Direccion:{id(lista1)} Lista 1: {lista1}")
#print(f"Direccion:{id(lista1)} Lista 2: {lista2}")


#lista1=[0,1,2,3,4]
#lista2=[5,6,7]
#lista1[5:]=lista2#[5,6,7]
#lista1[len(lista1):]=lista2
#lista1.append(20)
#print(lista1)

#insertar al inicio de la lista varios elementos (en una lista)
#lista1[:0]=lista2
#print(lista1)

#lista1.extend(lista2)
#lista1.append(lista2)
#print(lista1)
#
#del(lista1[0])
#print(lista1)
#
#del(lista1[2:5])
#print(lista1)
