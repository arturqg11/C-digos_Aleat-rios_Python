SegP = int(input("Digite a quantidade de segundos a ser convetida:"))
Dias = SegP // 86400
Horas = (SegP % 86400) // 3600
Min = ((SegP % 86400) % 3600) // 60
Seg = ((SegP % 86400) % 3600) % 60
print(Dias,"dias,",Horas,"horas,",Min,"minutos e",Seg,"segundos.")