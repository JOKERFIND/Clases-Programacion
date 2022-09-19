# Ejercicios en clase

## Escribir una funcion que reciba un mensaje y un nombre, ademas de escribir en pantalla "mensaje nombre"
#### def nombre(saludo:str, nmbr:str)->str:
####    print(saludo, nmbr)
####    return nombre
    
#### nmbr="Jose"
#### saludo="Buenos dias"
#### nombre(saludo, nmbr)
#### print("\n")

## Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser: "Hola 'nombre' tienes 'edad' años"
#### def sald(sl:str, nm:str, sl1:str, edad:str, sl2:str)->str:
####     print(sl, nm, sl1, edad, sl2)
####     return sald

#### sl="Hola"
#### sl1="tienes"
#### sl2="años"
#### nm=input("Ingrese su nombre: ")
#### edad=input("Ingrese su edad: ")

#### sald(sl, nm, sl1, edad, sl2)
#### print("\n")

## Hacer una funcion que reciba el nombre de una persona el año de nacimiento y el año de nacimiento y el año actual retornando el mensaje "Hola 'nombre', tienes edad años"
#### def edd(s:str, nb:str, s1:str, edd1:int, s2:str)->str:
####     print(f"{s} '{nb}' {s1} {edd1} {s2}")
####     return edd

#### s="Hola"
#### s1="tienes"
#### s2="años"
#### nb=input("Ingrese su nombre: ")
#### añoact=int(input("Ingrese el año actual: "))
#### añonc=int(input("Ingrese el año de nacimiento: "))
#### r=añoact-añonc
#### edd(s,nb,s1,r,s2)
#### print("\n")


## Hacer una funcion que reciba el nombre de una persona el año de nacimiento y el año actual retornando el mensaje "Hola 'nombre', tienes 'edad' años"


#### def presentacion(nombre:str, anc:int, anac:int)->str:
####  r=anac-anc
####  return f"Hola {nombre}, tienes {r} años"

#### def presentacion2(nombre:str, anc:int, anac:int)->str:
####  return f"Hola {nombre}, tienes {anac-anc} años"

#### def calcular_edad(anc:int, anac:int)->str:
####     return anac-anc

#### def presentacion3(nombre:str, anc:int, anac:int)->str:
####  return f"Hola {nombre}, tienes {calcular_edad(anc, anac)} años"

#### if __name__=="__main__":
####     print(presentacion("Ruben", 2002, 2022))
####     print(presentacion("Jose", 1999, 2022))
####     res=presentacion2("Antonio", 1974, 2022)
####     print(res)
####     print(presentacion("Alejandro", 1992, 2022))

## Realizar una funcion donde genere una tabla de multiplicar

#### def resultado(a:int, b:int)->int: return a*b
#### def tablas(m:int, q:int, fmt:int):
####     for i in range(1, m+1):
####         tabla(q, i, fmt)
####         print("")
#### def tabla(c:int, d:int, fmt:int):
####  for i in range(1, c+1):
####      print(F"{d:^{fmt}}*{i:^{fmt}}= {resultado(d, i):<{fmt}}")
     

#### if __name__=="__main__":    
####     print("\n")
####     tablas(3, 4, 6)
