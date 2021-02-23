# Nomes
# Pedro Henrique Fernandes Nishimura Pereira RA: 1903722
# Julio Teruyuki Noguchi Andres RA: 1903633

import json
from pprint import pprint

def pega_dados():
    with open('ano2018.json') as f:
        dados2018 = json.load(f)
    return dados2018

dados2018 = pega_dados()

'''
1. Crie uma função datas_de_jogo, que procura nos dados do 
brasileirão recebidas no parâmetro e devolve uma lista de todas 
as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do 
brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas 
as informações que foram lidas do arquivo JSON que acompanha 
essa atividade.
'''
def datas_de_jogo(dados):
    listaDatas = []
    for x in dados['fases']['2700']['jogos']['data']:
        listaDatas.append(x)
    return listaDatas
'''

2. Crie uma função data_de_um_jogo, que recebe a id numérica de 
um jogo e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a 
string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, 
o teste vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como 
strings)
'''
def data_de_um_jogo(dados, id_jogo):
    for x in dados['fases']['2700']['jogos']['id']:
        if (id_jogo == x):
            data = dados['fases']['2700']['jogos']['id'][id_jogo]['data']
            return data
    
    return 'não encontrado'
'''
3. Nos nossos dados, cada time tem um id, uma identificação 
numérica. (você pode consultar as identificações numéricas 
em dados['equipes']).

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas 
    em um único return.
'''
def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    time2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    return time1, time2

'''
4. A próxima função recebe a id_numerica de um time e deve 
retornar o seu 'nome-comum'.
'''
def nome_do_time(dados,id_time):
     nomeTime = dados['equipes'][id_time]['nome-comum']
     return nomeTime

'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id 
de um jogo e retorna os "nome-comum" dos dois times.
'''
def nomes_dos_times_de_um_jogo(dados, id_jogo):
    idTime1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    idTime2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    nomeTime1 = dados['equipes'][idTime1]['nome-comum']
    nomeTime2 = dados['equipes'][idTime2]['nome-comum']
    return nomeTime1, nomeTime2

'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.

Se o nome comum não existir, retorne 'não encontrado'.
'''
def id_do_time(dados,nome_time):
    for x in dados['equipes']['nome-comum']:
        if (nome_time == x):
            idTime = dados['equipes']['id']
            return idTime
    
    return 'não encontrado'

'''
7. Queremos procurar por 'Fla' e achar o Flamengo. 
Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''
def busca_imprecisa_por_nome_de_time(dados,nome_time):
    pass

'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''
def ids_de_jogos_de_um_time(dados,time_id):
    pass

'''
9. Usando as ids dos jogos em que um time participou, podemos 
descobrir em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''
def datas_de_jogos_de_um_time(dados, nome_time):
    pass

'''
10. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve um dicionário, com quantos gols cada time fez.
'''
def dicionario_de_gols(dados):
    pass

'''
11. A próxima função recebe apenas o dicionário dos dados do 
brasileirão.
Ela devolve a id do time que fez mais gols no campeonato.
'''
def time_que_fez_mais_gols(dados):
    pass

'''
12. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela devolve um dicionário. Esse dicionário conta, 
para cada estádio, quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    pass

'''
13. A próxima função recebe apenas o dicionário dos dados do 
brasileirão. Ela retorna o número de times que o brasileirão 
qualifica para a libertadores.Ou seja, devolve quantos times 
são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e 
você deve pegar esse número daí. Não basta retornar o valor 
correto, tem que acessar os dados fornecidos.
'''
def qtos_libertadores(dados):
    pass

'''
14. A próxima função recebe um valor com qtos times devem aparecer
na lista, e retorna esta lista, contendo as ids dos times melhor 
classificados.
'''
def ids_dos_melhor_classificados(dados, numero):
    pass

'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a 
classificação, quanto para obter o número correto de times 
a retornar.

A função só recebe os dados do brasileirão.
'''
def classificados_libertadores(dados):
      pass
'''
16. Da mesma forma que podemos obter a informação dos times 
classificados para a libertadores, também podemos obter os 
times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do 
brasileirão, e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''
def rebaixados(dados):
    pass

'''
17. A próxima função recebe (além do dicionario de dados 
do brasileirão) uma id de time.

Ela retorna a classificação desse time no campeonato.

Se a id nao for válida, ela retorna a string 'não encontrado'.
'''
def classificacao_do_time_por_id(dados, time_id):
    pass