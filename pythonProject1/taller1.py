#PROBLEMAS SECUENCIALES

#1
'''cap_inv=int (input("Digite su valor a invertir"))
gan=cap_inv*0.02

print("Su ganancia es de:", gan)

#2
sueldo_b=int (input("Digite su sueldo"))
venta1=int(input("Digite valor de la venta 1"))
venta2=int(input("Digite valor de la venta 2"))
venta3=int(input("Digite valor de la venta 3"))
venta_t=venta1+venta2+venta3
comisiones=venta_t*0.10
total_pa=sueldo_b+comisiones

print("\n Su ganancia por las ventas realizadas es de:", comisiones)
print("\n Y su pago en total es de:", total_pa)

#3
valor_com=int(input("Digite el valor de su compra"))
descuento=valor_com*0.15
total_pa=valor_com-descuento

print("EL valor de su compra con el descuento es de:", total_pa)

#4
cali1=float(input("Digite su calificación del parcial 1"))
cali2=float(input("Digite su calificación del parcial 2"))
cali3=float(input("Digite su calificación del parcial 3"))
exam_f=float(input("Digite su calificaión del examen final"))
traba_f=float(input("Digite su calificación del trabajo final"))
promedio=(cali1+cali2+cali3)/3
ppar=promedio*0.55
pexam_f=exam_f*0.30
ptraba_f=traba_f*0.15
cali_f=ppar+pexam_f+ptraba_f

print("La calificación final de su materia es:", cali_f)

#5
num_h=int(input("Digite el número de hombres"))
num_m=int(input("Digite el número de mujeres"))
total=num_h+num_m
porc_h=(num_h*100)/total
porc_m=(num_m*100)/total

print("El porcentaje de hombres es:", porc_h, "y el porcentaje de mujeres es:", porc_m)

#6
año_n=int(input("Digite su año de nacimiento"))
año_act=int(input("Digite el año actual"))
edad=año_act-año_n

print("Su edad es:", edad)

#PROBLEMAS PROPUESTOS

#1
cant_p=float(input("Digite su cantidad en pesos"))
dolares=0.00027
conv=cant_p*dolares

print("La equivalencia en dolares es de:", conv)

#2
numero=float(input("Digite el numero"))
if numero>=0:
    resultado=numero
    print("El valor absoluto es:", resultado)
else:
    resultado=-numero
    print("El valor absoluto es:", resultado)

#3
presion=float(input("Digite la presion"))
volumen=float(input("Digite el volumen"))
temperatura=float(input("Digite la temeratura"))
masa=(presion*volumen)/(0.37*(temperatura+460))

print("La masa de es de:", masa)

#4
edad=int(input("Digite su edad"))
num_pulsa=(220-edad)/10

print("El nivel de pulsaciones que usted debe de tener por cada 10s es de:", num_pulsa)

#5
salario_act=float(input("Digite su salario actual"))
incremento=0.25*salario_act
salario_t=salario_act+incremento

print("Su salario con el incremento del 25% es de:", salario_t)

#6
presupuesto=float(input("Digite el presupuesto"))
gine=presupuesto*0.40
trauma=presupuesto*0.30
pedia=presupuesto*0.30

print("El presupuesto designado para Ginecología es", gine, "para Traumatología", trauma, "y para Pediatría", pedia)

#7
precio_art=float(input("Digite el precio del artículo"))
ganancia=(precio_art*0.30)
venta=precio_art+ganancia

print("El precio de venta es:", venta)

#8
lunes=float(input("Digite el tiempo obtenido el día lunes"))
miercoles=float(input("Digite el tiempo obtenido el día miércoles"))
viernes=float(input("Digite el tiempo obtenido el día viernes"))
prom=(lunes+miercoles+viernes)/3

print("El tiempo promedio es de:", prom)

#9
per1=float(input("Digite la cantidad a invertir"))
per2=float(input("Digite la cantidad a invertir"))
per3=float(input("Digite la cantidad a invertir"))
total=per1+per2+per3
porc_per1=(per1*100)/total
porc_per2=(per2*100)/total
porc_per3=(per3*100)/total

print("El porcentaje invertido por la persona uno fue:", porc_per1, ",persona dos,", porc_per2, "y la de la persona tres", porc_per3)'''

#10
print("Materia matematicas")
exam_m=float(input("Digite la nota de su examen"))
tarea_1m=float(input("Digite la nota de su tarea 1"))
tarea_2m=float(input("Digite la nota de su tarea 2"))
tarea_3m=float(input("Digite la nota de su tarea 3"))
print("Materia Física")
exam_f=float(input("Digite la nota de su examen"))
tarea_1f=float(input("Digite la nota de su tarea 1"))
tarea_2f=float(input("Digite la nota de su tarea 2"))
print("Materia Quimica")
exam_q=float(input("Digite la nota de su examen"))
tarea_1q=float(input("Digite la nota de su tarea 1"))
tarea_2q=float(input("Digite la nota de su tarea 2"))
tarea_3q=float(input("Digite la nota de su tarea 3"))
porc_em=exam_m*0.90
prom_tm=((tarea_1m+tarea_2m+tarea_3m)/3)+0.10
total_m=porc_em+prom_tm
porc_ef=exam_f*0.80
prom_tf=((tarea_1f+tarea_2f)/2)+0.20
total_f=porc_ef+prom_tf
porc_eq=exam_q*0.85
prom_tq=((tarea_1q+tarea_2q+tarea_3q)/3)+0.15
total_q=porc_eq+prom_tq
prom_gene=(total_m+total_f+total_q)/3

print("Su promedio en matematicas es:", total_m, "\n En fisica", total_f, "\n En quimica", total_q)
print("\n Y su promedio general es de:", prom_gene )



















