# contém as funções para os menus
from operacoes import soma, subtracao, multiplicacao, divisao

def _exec_soma():
  n1 = float(input('Informe o primeiro número: '))
  n2 = float(input('Informe o segundo número: '))
  res = soma(n1, n2)
  print(f'A soma de {n1} e {n2} é: {res}')

def _exec_subtracao():
  n1 = float(input('Informe o primeiro número: '))
  n2 = float(input('Informe o segundo número: '))
  res = subtracao(n1, n2)
  print(f'A subtração de {n2} em {n1} é: {res}')

def _exec_multiplicacao():
  n1 = float(input('Informe o primeiro número: '))
  n2 = float(input('Informe o segundo número: '))
  res = multiplicacao(n1, n2)
  print(f'A multiplicação de {n1} por {n2} é: {res}')

def _exec_divisao():
  n1 = float(input('Informe o primeiro número: '))
  n2 = float(input('Informe o segundo número: '))
  res = divisao(n1, n2)
  print(f'A divisão de {n1} por {n2} é: {res}')

def print_menu():
  menus = ['1-Somar', '2-Subtrair', '3-Multiplicar', '4-Dividir', '0-Sair']
  str_menu = ''
  for menu in menus:
    str_menu += ' | '+menu
  print(str_menu)

def menu_sel(m: int):
  match m:
    case 0:
      print('Saindo...')
    case 1:
      _exec_soma()     
    case 2:
      _exec_subtracao()
    case 3:
      _exec_multiplicacao()
    case 4:
      _exec_divisao()