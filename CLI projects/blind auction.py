from system import os

#HINT: You can call clear() to clear the output in the console.

lances ={}

a=True
while a:
  nome = input("Qual o seu nome?\n")
  bid = int(input("Qual seu lance? (em R$)\n"))
  lances[nome] = bid
  system(clear)
  b=input('deseja inserir outro lance?(y/n)')
  if b == 'n' or b == 'N':
    a=False


def checa(lista):
  maior=0
  ganhador=''
  for i in lista:
    l =lances[i]
    if l > maior:
      maior = l
      ganhador = i
  print(f'{ganhador}: {maior}')

checa(lances)