# Thalita Fortes Domingos - 1644

import numpy as np

# Importando o dataset disponibilizado
space = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Exercício 1
# pega o maior numero da primeira linha ate o final da coluna zero
numeroMissoes = np.max(space[1:, 0].astype('int32'))

# copia do space para pegar o que precisa
mission_status = space[1:, 7].copy()

# procura na variavel passada as missoes que terminam com "Success"
status = np.char.endswith(mission_status,"Success")

# quantidade de missoes com sucesso
missoesSucesso = np.sum(status)

porcentagem = (missoesSucesso / numeroMissoes) * 100
print(f'\n{porcentagem:.3f}% das missões deram certo!') # 3 casas decimais


# Exercício 2
all_cost = np.array(space[1:, 6].astype('float32'))

# pegando a quantidade de valores maiores do que zero
num_cost_exc_0 = len(all_cost[all_cost > 0])

# somatorio dos valores maiores do que zero
sum_cost = sum(all_cost[all_cost > 0])

print(f'\nA média de gastos nas missões espaciais é de ${((sum_cost / num_cost_exc_0) * 100):.2f}.')


# Exercício 3
location = space[1:, 2] # percorre
missoesUSA = np.char.endswith(location, 'USA') # pega as localizacoes que terminam com 'USA'
numMissionsUSA = np.sum(missoesUSA)            # quantidade de missoes
print(f'\nEUA teve {numMissionsUSA} missões espaciais realizadas.')


# Exercício 4
missions_spaceX = space[1:,(1,6)]         # relaciona as colunas 1 e 6
# missions_spaceX é um novo array que inicia em 0,0
cond = missions_spaceX[0:,0] == "SpaceX"  # pega as da SpaceX que tem valor > 0
most_expensive = np.max(all_cost[cond])   # maior valor da SpaceX
print(f'\nA missão mais cara realizada pela SpaceX foi de ${(most_expensive):.2f}.')


# Exercício 5
companies = space[1:, 1]
print('\nEmpresas que já realizaram missões espaciais:')
all_companies = np.unique(companies) # unique pega os dados da coluna sem repeticao
for i in all_companies:
    # find passa o parametro de i para onde quer procurar (companies)
    var = np.char.find(companies, i)
    numMissoes = np.sum(var) + companies.size
    print(f'Company: "{i}" = {numMissoes} mission(s).')
