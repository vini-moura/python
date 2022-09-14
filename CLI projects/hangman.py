import random

word_list = ['azul', 'arvore', 'branco', 'estojo', 'lapis', 'termo', 'senso', 'nobre', 'algoz', 'etnia', 'icone', 'sobre',
             'solene', 'limiar', 'formal', 'comico', 'ciente', 'prazer', 'alocar', 'ocioso', 'tambem', 'eficaz',
             'empatia', 'embuste', 'conjuge', 'excecao', 'efemero', 'prolixo', 'carater', 'verbete', 'idilico', 'analogo',
             'conjuge', 'excecao', 'efemero','ambicao', 'conciso', 'coragem', 'parcial', 'imersao', 'modesto',
             'relacao', 'erudito', 'exotico', 'isencao','notorio', 'demanda', 'exilado', 'padecer', 'saudade',
             'colosso', 'escroto', 'volatil', 'auferir', 'inercia', 'colapso', 'ansioso', 'despota', 'difusao', 'intenso',
             'amizade', 'estirpe', 'emotivo', 'vigente', 'piedade', 'profano','inerente', 'peculiar', 'denegrir',
             'respeito', 'genocida', 'anuencia', 'deferido', 'prudente', 'equidade','sinonimo', 'concerne', 'alicerce',
             'despeito', 'retorica', 'destarte', 'fomentar', 'rechacar', 'proceder','desfecho', 'elegivel', 'sucumbir',
             'suscitar', 'complexo', 'perfidia', 'singular', 'escarnio', 'amalgama']

stage = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)
#test:
#print(f'the solution is {chosen_word}')

#variáveis
lives = 6
display = ['_' for c in chosen_word] #list comprehension

#jogo
print(f'a palavra tem {len(chosen_word)} letras')
while lives > 0:
    print(stage[lives])
    guess = input(f'Adivinhe uma letra: ').lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print(stage[0])
        end_game = True
        print('Você perdeu!')
        print(f'A palavra correta é {chosen_word}')

    if '_' not in display:
        end_game = True
        print('Você ganhou')
        break




