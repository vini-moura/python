# -*- coding: utf-8 -*-

print('''
**************
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
      % | |-%-------|
      % \ | %  ))   |
      %  \|%________|
***************
''')
print("Bem vindo à ilha do tesouro!\n Sua missão é encontrar o tesouro")

direção = input("Você está numa encruzilhada. Para qual lado deseja ir? 'e' ou 'd'").lower()

if direção == "e":
    print("\nVocê chegou num rio e no meio dele há uma ilha.\n Para atravessar há um barco furado ou uma ponte caindo.")
    direção = input("Você vai de barco ou pela ponte? 'B' ou 'P'").lower()
    if direção == "b":
        print("\nVocê chagou na ilha! À sua frente estão três cabanas, branca, vermelha e preta")
        direção = input("Qual você escolhe? 'b','v' ou 'p'").lower()
        if direção =="v":
            print("Parabéns, vocẽ venceu!")
        elif direção =="b":
            print("Os piratas estavam dentro.\n GAME OVER")
        else:
            print("Você deu de cara com um leão.\n GAME OVER")
    else:
        print("Você caiu da ponte e se afogou no rio.\n GAME OVER")
elif direção == "d":
    print("você deu de cara com um crocodilo. GAME OVER")
else:
    print("tecla errada, você deve escolher entre e ou d. GAME OVER")
