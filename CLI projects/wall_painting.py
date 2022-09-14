import math

def wall_painting(height,width,coverage):
      can = height*width/coverage
      can = math.ceil(can)
      print(f'voce precisará de {can} latas.')

altura = int(input('Qual a altura da parede? '))
largura= int(input('Qual a largura da parede? '))
cobertura = int(input('Qual a cobertura da tinta? '))

wall_painting(height=altura,width=largura,coverage=cobertura)
