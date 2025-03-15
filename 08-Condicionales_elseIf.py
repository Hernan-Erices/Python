#else if o elif se pueden ejecutar muchas condiciones

ingreso_mensual = 50
gasto_mensual = 90000

if ingreso_mensual > 10000:
	if ingreso_mensual - gasto_mensual > 20000:
		print("Ahora si que estas bien")
	else:
		print("Tas gastando mucho")

elif ingreso_mensual > 1000:
	print("estas decente")
elif ingreso_mensual > 100:
	print("Tas pobre")
else:
	print("Pobre pio pio")