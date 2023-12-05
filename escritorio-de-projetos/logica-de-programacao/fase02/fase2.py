import datetime
import locale
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

arq = open('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv', 'r')
arqArray = []

headersPosition = {
    "data": 0,
    "precip": 1,
    "maxima": 2,
    "minima": 3,
    "horas_insol": 4,
    "temp_media": 5,
    "um_relativa": 6,
    "vel_vent": 7,
}

for idx, linha in enumerate(arq):
    splited = linha.split(',')
    if (idx < 1):
        continue

    ultima = ''
    if splited[7].endswith('\n'):
        ultima = splited[7][:-1]
    else:
        ultima = splited[7]
    
    dataSplit = splited[0].split('/')
    dia = int(dataSplit[0])
    mes = int(dataSplit[1])
    ano = int(dataSplit[2])

    data = datetime.datetime(ano, mes, dia)

    tupla = (data.strftime('%d/%m/%Y'), splited[1], splited[2], splited[3], splited[4], splited[5], splited[6], ultima )

    arqArray.append(tupla)
arq.close()

# inicial

mesInicial = int(input('qual é o mês incicial? '))
while (mesInicial < 1) or (mesInicial > 12):
    print("mes incial inválido, por favor digite novamente o mes incial. O valor deve ser 1 até 12 ")
    mesInicial = int(input("Digite o mes incial "))

anoInicial = int(input('qual é o ano incicial? '))
while (anoInicial < 1961) or (anoInicial > 2016):
    print("Ano inicial inválido, por favor digite novamente o ano inicial. O valor deve ser 1961 até 2016 ")
    anoInicial = int(input("Digite o ano incial "))

diaInicial = int(input('qual é o dia incicial? '))

alcanceDataInicial = calendar.monthrange(anoInicial, mesInicial)
while diaInicial < 1 or diaInicial > alcanceDataInicial[1]:
    if  diaInicial > alcanceDataInicial[1]:
        print(f"Dia inicial inválido para o mês {calendar.month_name[mesInicial]}. O maior dia válido para este mês é {alcanceDataInicial[1]}.")
    else:
        print("dia inicial inválido, por favor digite novamente o dia inicial. O valor deve ser 1 até 31 ")
    diaInicial = int(input("Digite o dia inicial "))

# final

mesFinal = int(input('qual é o mês final? '))
while (mesFinal < 1) or (mesFinal > 12):
    print("mes final inválido, por favor digite novamente o mes final. O valor deve ser 1 até 12 ")
    mesFinal = int(input("Digite o mes final "))

anoFinal = int(input('qual é o ano final? '))
while (anoFinal < 1961) or (anoFinal > 2016):
    print("Ano inicifinal inválido, por favor digite novamente o ano final. O valor deve ser 1961 até 2016 ")
    anoFinal = int(input("Digite o ano incial "))

diaFinal = int(input('qual é o dia final? '))
alcanceDataFinal = calendar.monthrange(anoInicial, mesInicial)

while diaFinal < 1 or diaFinal > alcanceDataFinal[1]:
    if  diaFinal > alcanceDataFinal[1]:
        print(f"Dia final inválido para o mês {calendar.month_name[mesFinal]}. O maior dia válido para este mês é {alcanceDataFinal[1]}.")
    else:
        print("dia final inválido, por favor digite novamente o dia final. O valor deve ser 1 até 31 ")
    diaFinal = int(input("Digite o dia inicial "))


dataInicial = datetime.datetime(anoInicial, mesInicial, diaInicial)
dataFinal = datetime.datetime(anoFinal, mesFinal, diaFinal)

def mostrarOpcoes():
    print('Digite 1 para visualizar todos os dados')
    print('Digite 2 para visualizar apenas dados de precipitação')
    print('Digite 3 para visualizar apenas dados de temperatura')
    print('Digite 4 para visualizar apenas dados de vento e umidade do período informado')

def visualizarDados():
    numeroValido = False
    numeroEscolhido = 0

    while (numeroValido == False):
        mostrarOpcoes()
        numeroEscolhido = int(input())
        if (numeroEscolhido < 1 or numeroEscolhido > 4):
            print('Número inválido, digite novamente uma das opções')
            mostrarOpcoes()
            numeroEscolhido = int(input())
        else:
            numeroValido = True
    return numeroEscolhido

def opcao1():
    print(arqArray)

def opcao2(periodoSelecionado):
    for linha in periodoSelecionado:
        print(f'Precipitação: {linha[1]} volume por m²')

def opcao3(periodoSelecionado):
    for linha in periodoSelecionado:
        print(f'Temperatura: mínima de {linha[3]}ºC e máxima de {linha[2]}ºC')
def opcao4(periodoSelecionado):
    for linha in periodoSelecionado:
        print(f'Umidade: {linha[6]}% e vento {linha[7]}m/s')

def obterPeriodoSelecionado(dtInicio, dtFinal):
    periodoSelecionado = []
    idx = 0
    while idx < len(arqArray):
        dt = arqArray[idx][0]
        dataAtual = datetime.datetime.strptime(dt, '%d/%m/%Y')
        
        if dataAtual >= dtInicio and dataAtual <= dtFinal:
            periodoSelecionado.append(arqArray[idx])

        # Pula 6 itens no array para pegar a próxima data
        idx+= 6
    return periodoSelecionado

def obterMesMaiorPrecipitcao(periodoSelecionado):
    precipitacao = {
        'mes': '',
        'maiorPrecipitacao': 0
    }
    for linha in periodoSelecionado:
        if float(linha[1]) > precipitacao['maiorPrecipitacao']:
            precipitacao['mes'] = linha[0]
            precipitacao['maiorPrecipitacao'] = float(linha[1])
    
    mesFormatado = int(precipitacao['mes'].split('/')[1])
    print(f'O mes com maior precipitação foi {calendar.month_name[mesFormatado]}, com um valor de {precipitacao["maiorPrecipitacao"]} volume por m²')

# A - Visualização de intervalo de dados em modo texto
numeorEscolhido = visualizarDados()
if (numeorEscolhido == 1):
    opcao1()
if (numeorEscolhido == 2):
    opcao2(arqArray)
if (numeorEscolhido == 3):
    opcao3(arqArray)
if (numeorEscolhido == 4):
    opcao4(arqArray)
periodoSelecionado = obterPeriodoSelecionado(dataInicial, dataFinal)
# B - Mês menos chuvoso
obterMesMaiorPrecipitcao(arqArray)

#C - Média da temperatura mínina


def obterTemperaturasMinimas():
    idx = 0
    temperaturasMininas = []

    while idx < len(arqArray):
        mesSelecionado = mesInicial
        mesAtual = arqArray[idx][0].split("/")[1]
        
        if int(mesAtual) != mesSelecionado:
            idx += 6
            continue

        dataComeco = datetime.datetime(2006, mesSelecionado, 1)
        dataFinal = datetime.datetime(2016, mesSelecionado, 31)

        dataAtual = datetime.datetime.strptime(arqArray[idx][0], '%d/%m/%Y')

        if dataComeco <= dataAtual and dataFinal >= dataAtual:
            temperaturasMininas.append(float(arqArray[idx][3]))

            anoAtual = arqArray[idx][0].split("/")[2]
        idx += 6

    mediaTemperaturaMinimaTotal = sum(temperaturasMininas) / len(temperaturasMininas)

    print(f"A média da temperatura mínima em 11 anos é {mediaTemperaturaMinimaTotal:.2f}ºC")

obterTemperaturasMinimas()