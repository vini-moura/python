#import random
#num = random.randint(0,1)

#if num == 0:
#    print('Heads')
#elif num ==1:
#    print('tails')

import random
names_list = input("Insira os nomes dos participantes, separados por vírgula \n")
names_list = names_list.split(",")
a = len(names_list)
num = random.randint(0,a-1)
print(f"Quem pagará a conta é {names_list[num]}")
