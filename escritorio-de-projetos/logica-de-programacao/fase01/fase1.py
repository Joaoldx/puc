import locale
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

dadosArray = []

while (len(dadosArray) < 12):
    dadosObj = {}
    mes = int(input("Digite o mês "))
    while (mes < 1) or (mes > 12):
        print("Mes inválido, por favor digite novamente o mês. O valor deve ser entre 1 e 12 ")
        mes = int(input("Digite o mês "))

    dadosObj["mes"] = mes

    temperatura = float(input("Digite a temperatura em Celsius "))
    while (temperatura < -60) or (temperatura > 50):
        print("temperatura inválido, por favor digite novamente o mês. O valor deve ser entre -60 e 50 graus Celsius")
        temperatura = float(input("Digite a temperatura em Celsius "))

    dadosObj["temperatura"] = temperatura

    dadosArray.append(dadosObj)

mesQuente = ''
temperaturaMesQuente = -60

mesFrio = ''
temperaturaMesFrio = 50

quantidadeMesesQuentes = []
for current in dadosArray:
    if (temperaturaMesQuente <= current['temperatura']):
        temperaturaMesQuente = current['temperatura']
        mesQuente = int(current['mes'])
    
    if (temperaturaMesFrio >= current['temperatura']):
        temperaturaMesFrio = current['temperatura']
        mesFrio = int(current['mes'])

    if (current["temperatura"] > 38):
        quantidadeMesesQuentes.append(current["temperatura"])

temperaturaMedia = 0
if len(quantidadeMesesQuentes) > 0:
    temperaturaMedia = sum(quantidadeMesesQuentes) / len(quantidadeMesesQuentes)

print(f"O mês mais quente é {calendar.month_name[mesQuente]} com a temperatura de {temperaturaMesQuente}")
print(f"O mês mais frio é {calendar.month_name[mesFrio]} com a temperatura de {temperaturaMesFrio}")

if temperaturaMedia > 0:
    print(f"Ao todo foram {len(quantidadeMesesQuentes)} meses de altas temperaturas. A média das temperaturas desses meses mais quentes são de {temperaturaMedia}")
else:
    print("Não houve temperatura escaldante neste ano")