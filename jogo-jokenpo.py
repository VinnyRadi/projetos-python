import random
print('\033[1;32m='*10)
print('\033[1;36mJOKENPÔ')
print('\033[1;32m=\033[m'*10)

lista = [1, 2, 3]
maquina = (random.choice(lista))
print('''Selecione o que deseja jogar:
\033[1;36m[1]\033[m Pedra
\033[1;36m[2]\033[m Papel
\033[1;36m[3]\033[m Tesoura''')
p1 = int(input())

if p1 == maquina:
    print('Você jogou {} e a máquina jogou {}'.format(p1, maquina))
    print('\033[1;33mEMPATE!\033[m')
elif p1 == 1 and maquina == 2 or p1 == 2 and maquina == 3 or p1 == 3 and maquina == 1:
    print('Você jogou {} e a máquina jogou {}'.format(p1, maquina))
    print('\033[1;31mDERROTA!\033[m')
else:
    print('Você jogou {} e a máquina jogou {}'.format(p1, maquina))
    print('\033[1;32mVITÓRIA!\033[m')
