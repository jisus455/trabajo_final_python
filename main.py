from datetime import time

TIME_RECORD = time(4, 42, 15)
time_win = time(23, 59, 59)
num_win = 0
suma = 0

def getTime():
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    tiempo = time(horas, minutos, segundos)
    return tiempo

# def obtener_tiempo():
#     tiempo = input("Ingrese tiempo [hh(00-23)/mm(00-59)/ss(00-59)]: ")
#     hour = int(tiempo[0:2])
#     min = int(tiempo[3:5])
#     seg = int(tiempo[6:8])
#     return time(hour, min, seg)

part = int(input("Ingrese cantidad participantes: "))
for i in range(part):
    num = int(input("Ingrese un numero: "))
    tiempo = getTime()
    if tiempo < time_win:
        time_win = tiempo
        num_win = num
        time_record = time_win
    
    suma += tiempo.hour * 3600 + tiempo.minute * 60 + tiempo.second

if num != 0:
    print("El numero ganador de la carrera:", num_win, "y tiempo que empleo:", time_win)
    time_seconds = (suma/part)
    
    time_hour = time_seconds // 3600
    time_seconds %= 3600

    time_minute = time_seconds // 60
    time_seconds %= 60

    time_average = time(int(time_hour), int(time_minute), int(time_seconds))
    print("Tiempo promedio entre ciclistas:", time_average)

print("Ingrese record")
record = getTime()
if record < time_record:
    print("Nuevo tiempo record! el ganador batio el record")
