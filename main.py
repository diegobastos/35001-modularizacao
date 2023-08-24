# main.py -> o arquivo principal do projeto
#do arq. menu importe as funõeso print_menu e menu_sel
from menu import print_menu, menu_sel

# ponto de início do app
if __name__ == '__main__':
  print('Calculadora do Diego')
  print_menu()
  menu = int(input('Opção: '))
  menu_sel(menu) 