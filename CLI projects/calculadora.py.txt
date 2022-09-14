from art import logo
print(logo)
def soma(n1,n2):
  return(n1+n2)
def menos(n1,n2):
  return(n1-n2)
def vezes(n1,n2):
  return(n1*n2)
def divide(n1,n2):
  return(n1/n2)

def calculadora(a,b,c):
  a= True
  while a:
    if b=='+':
      return(soma(a, c))
    elif b =='+':
      return(menos(a, c))
    elif b=='*':
      return(vezes(a, c))
    elif b=='/':
      return(divide(a, c))
    else:
      return("Operação inválida")
    m=input('novo cálculo?')
    if m == 'n':
      a=False
    else:
      clear()


x=int(input('Qual o primeiro nº?  '))
y=input('Qual a operação? (+ - * /)  ')
z=int(input('Qual o segundo nº?  '))
print(calculadora(x,y,z) )