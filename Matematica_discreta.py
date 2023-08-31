'''
ACADEMICOS:

GABRIEL BERTO BECKAUSER
LUCAS DE OLIVEIRA CUNHA
VICTOR EDUARDO SURMACZ

Segue código referente ao trabalho feito em sala no dia 31/08/2023.
Trabalho entregue com atraso por conta do travamento dos computadores em sala de aula, prejudicando a execução e o entendimento do trabalho.
'''
arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.readlines()
contador = 0
quantidade_linhas = len(conteudo)

for i in range(quantidade_linhas):
  if conteudo[i][0] == "U":
    conjunto_A_uniao = conteudo[i + 1].replace(",", "").split()
    conjunto_B_uniao = conteudo[i + 2].replace(",", "").split()
    conjunto_A_uniao = set(conjunto_A_uniao)
    conjunto_B_uniao = set(conjunto_B_uniao)
    conjunto_uniao = conjunto_A_uniao.union(conjunto_B_uniao)

  if conteudo[i][0] == "I":
    conjunto_A_inter = conteudo[i + 1].replace(",", "").split()
    conjunto_B_inter = conteudo[i + 2].replace(",", "").split()
    conjunto_A_inter = set(conjunto_A_inter)
    conjunto_B_inter = set(conjunto_B_inter)
    conjunto_inter = conjunto_A_inter.intersection(conjunto_B_inter)

  if conteudo[i][0] == "D":
    conjunto_A_diferenca = conteudo[i + 1].replace(",", "").split()
    conjunto_B_diferenca = conteudo[i + 2].replace(",", "").split()
    conjunto_A_diferenca = set(conjunto_A_diferenca)
    conjunto_B_diferenca = set(conjunto_B_diferenca)
    conjunto_diferenca = conjunto_A_diferenca.difference(conjunto_B_diferenca)

  if conteudo[i][0] == "C":
    conjunto_A_cart = conteudo[i + 1].replace(",", "").split()
    conjunto_B_cart = conteudo[i + 2].replace(",", "").split()
    conjunto_cart = []
    for j in range(len(conjunto_A_cart)):
      for k in range(len(conjunto_B_cart)):
        string_cart = (conjunto_A_cart[j], conjunto_B_cart[k])
        conjunto_cart.append(string_cart)
    conjunto_A_cart = set(conjunto_A_cart)
    conjunto_B_cart = set(conjunto_B_cart)
    conjunto_cart = set(conjunto_cart)


print("União: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(conjunto_A_uniao, conjunto_B_uniao, conjunto_uniao))
print("Interseção: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(conjunto_A_inter, conjunto_B_inter, conjunto_inter))
print("Diferença: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(conjunto_A_diferenca, conjunto_B_diferenca, conjunto_diferenca))
print("Produto Cartesiano: conjunto 1 {}, conjunto 2 {}. Resultado: {} ".format(conjunto_A_cart, conjunto_B_cart, conjunto_cart))
