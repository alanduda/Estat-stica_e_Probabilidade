import matplotlib.pyplot as plt
from math import factorial
import random

# infelizmente não consegui encontrar um dataset diferente do que o senhor passou no video sobre diagnostico com variável de Bernoulli
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
print(f'E(x) = p = Chance de dar Coroa = {p}')
print(f'q = {q:0.3f}')

# VAR(x)
pq = p * q
print(f'VAR(x) = p . q = {pq:0.3f}')

#Calcular Média
n = 5  #numero de tentativas
average = n * p
print(f'Media = E(x) = {average}')

#Calcular Variância
variance = n * p * q
print(f'Variância = VAR(x) = {variance}')

#Calcular desvio padrão
standardDeviation = variance**0.5
print(f'Desvio Padrão = {standardDeviation}')

# Calcular probabilidade binomial
odds = []
def binomialProbability(x,n,p,q):
  return (factorial(n)/(factorial(n-x)*factorial(x)))*(p**x)*(q**(n-x))

for x in range(6):
    px = binomialProbability(x,n,p,q)
    print('P(',x,')=',px)
    odds.append(px)

print('Apartir dos resultados abaixo é possivel perceber que a maior probabilidade do jogar tirar uma sequenciade de acerto seria 3 jogadas')
x = [0,1,2,3,4,5]
plt.bar(x,odds)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Distribuição de Probabilidade')
plt.grid(True)
plt.show()