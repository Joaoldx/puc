### Enunciado da fase 2

Novamente vamos trabalhar com dados meteorológicos, mas agora os dados serão de um arquivo texto.  Nesta fase, você trabalhará com um conjunto de dados¹ (formato csv² em anexo disponibilizado no Material Complementar) contendo informações climáticas diárias do município brasileiro de Porto Alegre, entre os anos 1961 e 2016. O arquivo contém 18.564 registros com os campos: data, precipitação (volume de chuva em milímetros por m2), temperatura máxima (em graus celsius), temperatura mínima (em graus celsius), umidade relativa do ar (% entre 0 e 100) e a velocidade do vento (em m/s). 

 

Seu programa deve ser capaz de realizar:

 

- Carga e preparação de dados: trabalhar com arquivos de dados, realizando a sua leitura, filtragem das informações relevantes e armazenamento em estruturas de dados adequadas para consulta. 

- Análise e visualização de dados: análises estatísticas diversas sobre os dados armazenados, por meio da implementação de algoritmos e geração de gráficos para a visualização dos resultados.

 

O código entregue em linguagem Python deve permitir:

 

Leitura do arquivo: os dados do arquivo devem ser carregados para memória e disponibilizados em uma lista de listas/tuplas/dicionário.
   

Observações: 

- É a partir da aula 08 que explicamos como realizar a leitura de arquivo texto e a carga dos dados em listas. No entanto, a manipulação de estruturas de dados está nas aulas anteriores à aula 08. Por isso, é importante você assistir e realizar as práticas na sequência sugerida. Nossos exemplos são todos com arquivo CSV e não há necessidade de uso de bibliotecas específicas, além das abordadas na disciplina. Além das funções de manipulação de arquivo, funções strings, como split, serão essenciais para a carga dos dados em lista/dicionário. No entanto, você pode usar outras bibliotecas se já conhecê-las.

- Crie quantas estruturas de dados (listas, dicionários, ...) que você julgar conveniente e não esqueça de organizar seu código em funções. 

- Comente no seu código decisões tomadas quanto ao tratamento dos dados. Não use caminhos absolutos para o arquivo .csv, implemente considerando que o arquivo está na mesma pasta do seu programa. Não defina caminhos específicos dentro do seu código para acesso ao arquivo .csv. Se você entregar com caminhos absolutos o trabalho não será avaliado. 

- Não modifique o arquivo .csv dado. Seu programa é que deve tratar os dados lidos do arquivo.

 

a) Visualização de intervalo de dados em modo texto: a partir de entradas do usuário, sua implementação deve permitir a visualização dos dados que foram carregados do arquivo. O usuário deve informar o período que quer ver, ou seja, deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. Permita também que o usuário informe se quer ver 1) todos os dados, 2) apenas os de precipitação, 3) apenas os de temperatura, ou 4) apenas os de umidade e vento para o período informado. 

 

Observações: 

- Valide os dados de entrada;

- Você pode escolher a forma de apresentação dos dados, porém não esqueça de incluir um cabeçalho para os dados exibidos.

 

b) Mês menos chuvoso: o mês/ano com menor precipitação, considerando todos os dados do arquivo. Exiba também a menor precipitação na tela. Utilize obrigatoriamente um dicionário e implemente ao menos uma função.  Lembre-se de considerar todos os dados do arquivo! 

 

c) Média da temperatura mínima de um determinado mês (auge do inverno) nos últimos 11 anos (2006 a 2016): 

1) o programa deve escrever a média da temperatura mínima de um mês informado pelo usuário (valide a entrada) e a média geral da temperatura mínima para todo o período (11 anos). Se o mês informado for 8, ou seja, agosto, o programa exibir a temperatura mínima média do mês de agosto de cada ano (agosto/2006, agosto/2007, ...agosto/2016), 

2) o programa também deve escrever qual é a média geral da temperatura mínima que engloba todos os meses de agosto desse período de 11 anos. Implemente ao menos uma função para estes itens e use dicionário. 

 

d) Gráfico de barras (vertical ou horizontal) com as médias de temperatura mínima de um determinado mês nos últimos 11 anos. Gere um gráfico com as médias calculadas do mês informado em cada ano do período conforme o item d. Não esqueça de rotular os eixos e usar legendas para deixar o seu gráfico informativo e bem elaborado.


O que você precisa entregar: um .zip contendo o seu código em Python, ou seja, zipe seu .py ou .ipynb e poste na plataforma. Dentro do .zip só pode conter o arquivo em Python, não pode estar dentro de uma pasta. Lembre que seu programa deve executar acessando o arquivo .csv localmente!

ATENÇÃO AO FORMATO DO ARQUIVO: Você deve submeter seu arquivo exclusivamente no formato ZIP. Não é possível submeter outros formatos de arquivos compactados, como RAR, por exemplo.

 

Quais aulas você deve assistir para realizar esta fase do projeto: assistir e realizar as práticas das aulas 1 a 10 para desenvolver esta fase do projeto.

 

____________________________________________

¹ Os dados foram obtidos em https://bdmep.inmet.gov.br/

² CSV ou “comma-separated-values” (valores separados por vírgulas) é a extensão usada para arquivos-texto nos quais os dados estão dispostos em colunas e algum caracter é utilizado como separador dessas colunas. O separador mais usual são as vírgulas, mas pode ser qualquer também ponto-e-vírgula (;), hífen (-), TAB, espaços em branco, etc.