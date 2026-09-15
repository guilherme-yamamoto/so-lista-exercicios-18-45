hora_inicial = int(input("Insira a hora inicial que começa o jogo: "))
minuto_inicial = int(input("Insira o minuto inicial que começa o jogo: "))

hora_final = int(input("\nInsira a hora final que termina o jogo: "))
minuto_final = int(input("Insira o minuto final que termina o jogo: "))

tempo_hora = hora_final - hora_inicial
tempo_minuto = minuto_final - minuto_inicial

if(hora_inicial > hora_final):
    tempo_hora = (24 - hora_inicial) + hora_final
if(minuto_inicial > minuto_final):
    tempo_minuto = (60 - minuto_inicial) + minuto_final
    tempo_hora = tempo_hora - 1

print(f"O jogo vai durar {tempo_hora}h e {tempo_minuto}min.")