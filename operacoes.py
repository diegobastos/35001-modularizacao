# Contém a implementação das 4 operações básicas
def soma(n1, n2):
  return n1 + n2

def subtracao(n1, n2):
  return n1 - n2

def multiplicacao(n1, n2):
  return n1 * n2

def divisao(n1, n2):
  if n2 == 0:
    return 'Não é possível dividir por zero'
  else:
    return n1 / n2