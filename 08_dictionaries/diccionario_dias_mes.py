dias_por_mes = {
    "Enero": 31,
    "Febrero": 28,
    "Marzo": 31,
    "Abril": 30,
    "Mayo": 31,
    "Junio": 30,
    "Julio": 31,
    "Agosto": 31,
    "Septiembre": 30,
    "Octubre": 31,
    "Noviembre": 30,
    "Diciembre": 31
}
print(dias_por_mes)
for mes, dias in dias_por_mes.items():
    print(f'{mes} tiene {dias} días')
