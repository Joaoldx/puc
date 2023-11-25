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

diaInicial =  10 # int(input('qual é o dia incicial? '))
mesInicial =  10 # int(input('qual é o mês incicial? '))
anoInicial =  2000 # int(input('qual é o ano incicial? '))

diaFinal =  10 # int(input('qual é o dia final? '))
mesFinal =  10 # int(input('qual é o mês final? '))
anoFinal =  2002 # int(input('qual é o ano final? '))

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
for idx, linha in enumerate(arqArray):
    mesSelecionado = mesInicial
    anoSelecionado = anoInicial
    dataComeco = datetime.datetime(anoSelecionado, mesSelecionado, 1)
    dataFinal = datetime.datetime(anoSelecionado, mesSelecionado, 31)

    if dataComeco >=  datetime.datetime.strptime(linha[0], '%d/%m/%Y'):
        print(linha[0])