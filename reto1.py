#Ejercicio #1
dia = input("Ingrese el día de la semana (lunes, martes, miércoles, jueves, viernes, sábado, domingo): ").lower()
tiempo = int(input("Ingrese el tiempo de estacionamiento en minutos: "))

dias_ = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
if dia not in dias_:
    print("Día de la semana no existe!!")
else:
    if tiempo <= 0:
        print("Error: El tiempo de estacionamiento debe ser mayor que 0 minutos")
    else:
        if dia == "lunes" or dia == "martes" or dia == "miércoles":
            tarifa = 2.00
        elif dia == "jueves" or dia == "viernes":
            tarifa = 2.50
        else:
            tarifa = 3.00
        total = tiempo / 60 * tarifa

        print("El cliente debe pagar $" + str(total))


