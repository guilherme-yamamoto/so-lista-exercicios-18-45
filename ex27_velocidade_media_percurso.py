voltas = int(input("Insira a quantidade de voltas realizadas: "))
circuito = float(input("Insira a extensão do circuito (em metros): "))
duracao = int(input("Insira o tempo do percurso (em minutos apenas): "))
velocidade_media = ((circuito * voltas) / (duracao * 60)) * 3.6

print(f"\nQuantidade de Voltas: {voltas} / Extensão do Circuito: {circuito} / Duração do Percurso: {duracao} \nA velocidade média é de {velocidade_media}km/h")