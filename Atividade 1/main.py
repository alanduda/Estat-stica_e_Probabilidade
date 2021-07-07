from prettytable import PrettyTable
import matplotlib.pyplot as plt
import csv
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

# Este DataSet tem os dados de vendas de um supermercado inaugurado em Guanajuato, México.
# Iremos pegar os valores totais de cada venda
with open(dir_path + '/' + 'Sales.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader.__next__()
    sales = []
    for row in csv_reader:
        sales.append(float(row[3]))

# Passo 1: escolher um número de classes
n_classes = 5

# Passo 2: Calcular amplitude dos dados
bigger = max(sales)
smaller = min(sales)
breadth = bigger - smaller

# Passo 3: Calcular amplitude de cada classe
classBreadth = round(breadth/n_classes)

# Passo 4: Calcular os limites de classes
inferiorLimits = [smaller]
upperLimits = []
for i in range(n_classes):
    inferiorLimits.append(inferiorLimits[i]+classBreadth)
    upperLimits.append(inferiorLimits[i]+classBreadth-1)

# Passo 5: calcular as ocorrências nas classes
frequencies = {'class1': 0, 'class2': 0, 'class3': 0, 'class4': 0, 'class5': 0}
for sale in sales:
    if sale < inferiorLimits[1]:
        frequencies['class1'] +=1
    elif sale < inferiorLimits[2]:
        frequencies['class2'] +=1
    elif sale < inferiorLimits[3]:
        frequencies['class3'] +=1
    elif sale < inferiorLimits[4]:
        frequencies['class4'] +=1
    else:
        frequencies['class5'] +=1

table = PrettyTable(['classe', 'frequência'])

for i in range(5):
    table.add_row([f'{int(inferiorLimits[i])}-{int(upperLimits[i])}', f"{frequencies[f'class{i+1}']}"])

# Tabela com valores absolutos
print(table)

frequencies2 = {'class1': 0, 'class2': 0, 'class3': 0, 'class4': 0, 'class5': 0}
n_occurrences = len(sales)
for _class in frequencies:
    frequencies2[_class] = frequencies[_class]/n_occurrences

table2 = PrettyTable(['classe', 'frequência', '%'])
for i in range(5):
    table2.add_row([f'{int(inferiorLimits[i])}-{int(upperLimits[i])}', f"{(frequencies[f'class{i+1}']*100):0.1f}",f"{(frequencies2[f'class{i+1}']*100):0.1f}"])

# Tabela com valores absolutos e relativos
print(table2)

print('Apartir do resultado dos dados é possivel perceber que 96.5% do total das vendas do supermercado fica abaixo de 1000 Pesos mexicanos. \nAo contário de compras com valor total entre 3000 e 4000 pesos mexicanos que tem uma frequencia nenhuma.')

plt.hist(sales, 5)
plt.xlabel('Classes')
plt.ylabel('Quantidade')
plt.title('Ocorrências das Classes')
plt.grid(True)
plt.show()