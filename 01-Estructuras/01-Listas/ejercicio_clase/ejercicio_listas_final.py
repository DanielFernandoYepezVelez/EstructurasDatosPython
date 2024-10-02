""" Una empresa llamada “Transportes Cesde” requiere guardar 
los nombres de los conductores y el dinero que recaudan 
cada día de la semana (lun a sábado) movilizando a la comunidad 
educativa y el porcentaje de recaudo de cada conductor.  
Para guardar esta información se crearán las siguientes listas:  
NombreConductor: para almacenar los nombres de los conductores.  
DiasSemana: que contiene los días de lunes a sábado.  
Recaudo: lista para guardar la cantidad recolectada cada día 
de la semana. Se debe generar una lista llamada total recaudo 
con la suma total de lo recaudado por cada conductor.  
Debe solicitar el número de conductores que hacen parte de 
la empresa de Transporte Cesde. """

# Definir E Inicializar Variables O Constantes
index = 0
acumulator_tax_driver = 0

general_tax = []
driver_names = []
tax_driver_day = []
tax_driver_percent_final = []
days_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado']

# Solicitar Información Por Consola
driver_quantity = int(input('Ingrese La Cantidad De Conductores: '))

while (index < driver_quantity):
    # Ingresar Información Por Consola
    name = input(f'\nIngrese El Nombre Del Conductor #{index + 1}: ')

    # Adjuntando Los Resultados En La Lista De Nombres
    driver_names.append(name)

    for j in range(len(days_week)):
        tax_day = float(input(f'Ingrese El Dinero Recaudado El Día {days_week[j]}: '))        
        driver_percent = int(input('Ingrese El Porcentaje Ganado Por El Conductor: '))

        # Proceso Aritméticos
        tax_driver_percent =  tax_day * (driver_percent / 100)
        acumulator_tax_driver += tax_driver_percent 
        
        # Adjuntando Los Resultados Finales En Las Listas Creadas
        general_tax.append(tax_day)
        tax_driver_day.append(tax_driver_percent)
        tax_driver_percent_final.append(driver_percent)
    
    index += 1

print('\n\t\t\t\t\t\t\t=================================')
print('\t\t\t\t\t\t\t======= TRANSPORTES CESDE =======')
print('\t\t\t\t\t\t\t=================================')

# Mostrar Información Por Consola De Las Listas Preliminar
print('\n===== Reporte Preliminar =====')
print(f'Nombre De Los Conductores: {driver_names}')
print(f'Impuesto Recaudado Diariamente: {general_tax}')
print(f'Porcentaje Del Conductor Por El Impuesto Recaudado: {tax_driver_percent_final}')
print(f'Impuesto Recaudado Diariamente Del Conductor: {tax_driver_day}')
print(f'Impuesto Total De Los Conductores: {acumulator_tax_driver}')

# Mostrar Información Por Consola De Las Listas Preliminares
print('\n===== Reporte Final =====')
for index in range(len(driver_names)):
    for day, tax_value, tax_percent, tax_driver in zip(days_week, general_tax, tax_driver_percent_final, tax_driver_day):
        print(f'El Conductor {driver_names[index]} El Día {day} Recaudo El Valor De {tax_value} Pesos,'
              f'A El Conductor {driver_names[index]} Le Corresponde El {tax_percent}%.'
              f'Que Es Equivalente A: {tax_driver} Pesos.')
    
    print('\n')

print(f'Y El Total Recaudado Diariamente Por Todos Los Conductores Son: {acumulator_tax_driver} Pesos.')