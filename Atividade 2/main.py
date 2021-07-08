import random

# infelizmente não consegui encontrar um dataset com variável de Bernoulli
# por isso, criei um dataset no qual ha um probabilidade de uma moeda cair cara(0) ou coroa(1)
dataset = [[i, random.choice([0, 1])] for i in range(1000)]

# Amostragem aleatoria
randomSampling = random.sample(dataset, 50)

# Amostragem Estrátificada
list1 = dataset[50:100]
list2 = dataset[450:500]
list3 = dataset[850:900]

stratifiedSampling = []

stratifiedSampling += random.sample(list1, 20)
stratifiedSampling += random.sample(list2, 20)
stratifiedSampling += random.sample(list3, 20)

# Amostragem Sistemática
coins = [i for i in range(1000)]
selectedCoins = [dataset[i] for i in range(0, len(coins), 10)]

# descobrindo p e q, supondo que p seja vitoria (coroa)
numberHeads = 0
numberTails = 0
for x in dataset:
    if(x[1] == 0):
        numberHeads += 1
    else:
        numberTails += 1
# E(x)
p = numberHeads/len(dataset)
q = numberTails/len(dataset)
print(f'E(x) = p = Chance de dar Coroa = {p*100:0.2f}%')
print(f'q = {q:0.3f}')

# VAR(x)
pq = p * q
print(f'VAR(x) = p . q = {pq:0.3f}')

# Calcular probabilidade binomial
