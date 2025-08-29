tiempo_en_segundos = int(input(" cuales el tiempo en segundos?: "))
if (tiempo_en_segundos<600):
    missing_seconds= 600 - tiempo_en_segundos
    print(f'faltan {missing_seconds} segundos')
elif(tiempo_en_segundos>600):
    print("mayor")
elif(tiempo_en_segundos == 600):
    print("igual")    