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
la empresa de Transporte Cesde.  """

print('======= TRANSPORTES CESDE =======')

# Definir E Inicializar Variables O Constantes
tax = []
index = 0
acumulator = 0
driver_names = []
tax_driver_day = []
total_tax_driver_day = []
days_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado']

# Solicitar Información Por Consola
driver_quantity = int(input('Ingrese La Cantidad De Conductores: '))

while (index < driver_quantity):
    # Ingresar Información Por Consola
    name = input(f'\nIngrese El Nombre Del Conductor #{index + 1}: ')
    tax_day = float(input(f'Ingrese El Dinero Recaudado El Día {days_week[index]}: '))
    driver_percent = float(input('Ingrese El Porcentaje Ganado Por El Conductor: '))

    # Proceso Aritméticos
    tax_driver_percent =  tax_day * (driver_percent / 100)
    acumulator += tax_driver_percent 
    
    # Adjuntando Los Resultados Finales En Las Listas Creadas
    driver_names.append(name)
    tax.append(tax_day)
    tax_driver_day.append(tax_driver_percent)
    
    index += 1

total_tax_driver_day.append(acumulator)

# Mostrar Información Por Consola De Las Listas Finales
print('\n===== Reporte Preliminar =====')
print(f'Nombre De Los Conductores: {driver_names}')
print(f'Impuesto Recaudado Diariamente: {tax}')
print(f'Impuesto Recaudado Diariamente Del Conductor: {tax_driver_day}')
print(f'Impuesto Total De Los Conductores: {total_tax_driver_day}')

print('\n===== Reporte Final =====')
# for names, tax, tax_driver, total_tax_driver in zip(driver_names, tax, tax_driver_day, total_tax_driver_day)