#Operadores Matemáticos - SUMA

py = 3.1416
variable1 = 2018
variable2 = 0.9999

print(py+variable1+variable2)

#Operadores Matemáticos - RESTA

total_ganado = 4000
aportes_laborales = 500
prestamos = 300

print(total_ganado - aportes_laborales - prestamos)

#Operadores Matemáticos - MULTIPLICACIÓN

total_ganado = 4000
bono_antiguedad = 0.1 #(10%)

print(total_ganado * bono_antiguedad)

#Operadores Matemáticos - DIVISIÓN

total_manzanas = 1234
total_familias = 81

print(total_manzanas / total_familias)

#Operadores Matemáticos - RESTO DE LA DIVISIÓN

dividendo_exacta = 200
divisor_exacta = 2

print(dividendo_exacta % divisor_exacta) #división exacta

dividendo_inexacta = 10
divisor_inexacta = 7

print(dividendo_inexacta % divisor_inexacta) #división inexacta


#Operadores Lógicos - Mayor que

print(3>1) #3 es mayor que 1 True (Verdadero)
print(1>3) #1 es mayor que 3 False (Falso)

#Operadores Lógicos - Menor que

print(7<1) #7 es menor que 1 False (Falso)
print(1<7) #1 es menor que 7 True (Verdadero)



#Operadores Lógicos - Mayor o Igual que

print(3>=10) #3 es mayor o igual que 10 False (Falso)
print(3>=3) #3 es mayor o igual que 3 True (Verdadero)   
print(3>=1) #3 es mayor o igual que 1 True (Verdadero)  


#Operadores Lógicos - Menor o Igual que

print(1<=8) #1 es menor o igual que 8 True (Verdadero)  
print(1<=1) #1 es menor o igual que 1 True (Verdadero)  
print(8<=1) #8 es menor o igual que 1 False (Falso)  

#Operadores de Comparación - Igualdad

print(1==2) #1 es igual a 2 False (Falso) 
print(2==2) #2 es igual a 2 True (Verdadero)  

#Operadores de Comparación - Desigualdad

print(40!=39) #40 es diferente a 39 True (Verdadero) 
print(39!=39) #39 es diferente a 39 False (Falso)

#Operadores de Comparación - AND

caso1 = 11==11 and 13==13
print(caso1) 

caso2 = 3*9!=3%6 and (56%9)==(100*(3%3))
print(caso2)

caso3 = (56%8)==(100*(3%3)) and 7%77 == 54
print(caso3)

caso4 = 3*12 == 1 and 77%7 == 54
print(caso4)
#Operadores de Comparación - OR

caso1 = (56%7)==(100*(3%3)) or 33%3!=1
print(caso1) 

caso2 = (56%7)==(100*(3%3)) or (3*3) != 9
print(caso2)

caso3 = 34==1 or (56%7)==(100*(3%3))
print(caso3)

caso4 = 22!=22 or 11!=11
print(caso4)




