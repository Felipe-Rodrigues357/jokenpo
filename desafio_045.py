import emoji

import time

import random

print('\033[1;4;34m=================JOKENPÔ=================\033[m')
jogador = int(input(emoji.emojize('\033[1;30mOPÇÕES DE JOGADA:'
                                  '\n(1):fist:'
                                  '\n(2):raised_hand:'
                                  '\n(3):v:'
                                  '\nESCOLHA A SUA JOGADA: \033[m', use_aliases=True)))
computador = random.randint(1, 3)
processando = '\033[1;4;33mPROCESSANDO....\033[m'
for char in processando:
    print(char, end='')
    time.sleep(.25)
print('\033[1;30m\nOPÇÕES DE JOGADA:')
print(emoji.emojize('(1):fist:', use_aliases=True))
print(emoji.emojize('(2):raised_hand:', use_aliases=True))
print(emoji.emojize('(3):v:', use_aliases=True))
print('ESCOLHA A SUA JOGADA: \033[m', end='')
print('\033[1;4;33m{}\033[m.'.format(computador))
print('\033[1;4;31m===============RESULTADO===============\033[m')
if computador == 1 and jogador == 3:
    print(emoji.emojize('\033[1;4;33mCOMPUTADOR:\033[m :fist: \033[1;30mVS\033[m '
                        ':v: \033[1;34m:VOCÊ\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;4;33mCOMPUTADOR VENCEU \033[m:thumbsdown:', use_aliases=True))
elif computador == 2 and jogador == 1:
    print(emoji.emojize('\033[1;4;33mCOMPUTADOR:\033[m :raised_hand: \033[1;30mVS\033[m '
                        ':fist: \033[1;34m:VOCÊ\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;4;33mCOMPUTADOR VENCEU \033[m:thumbsdown:', use_aliases=True))
elif computador == 3 and jogador == 2:
    print(emoji.emojize('\033[1;4;33mCOMPUTADOR:\033[m :v: \033[1;30mVS\033[m '
                        ':raised_hand: \033[1;34m:VOCÊ\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;4;33mCOMPUTADOR VENCEU \033[m:thumbsdown:', use_aliases=True))
elif jogador == 1 and computador == 3:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :fist: \033[1;30mVS\033[m '
                        ':v: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;34mVOCÊ VENCEU \033[m:metal:', use_aliases=True))
elif jogador == 2 and computador == 1:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :raised_hand: \033[1;30mVS\033[m '
                        ':fist: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;34mVOCÊ VENCEU \033[m:metal:', use_aliases=True))
elif jogador == 3 and computador == 2:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :v: \033[1;30mVS\033[m '
                        ':raised_hand: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;34mVOCÊ VENCEU \033[m:metal:', use_aliases=True))
elif jogador == 1 and computador == 1:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :fist: \033[1;30mVS\033[m '
                        ':fist: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;31mEMPATE \033[m:ok_hand:', use_aliases=True))
elif jogador == 2 and computador == 2:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :raised_hand: \033[1;30mVS\033[m '
                        ':raised_hand: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;31mEMPATE \033[m:ok_hand:', use_aliases=True))
elif jogador == 3 and computador == 3:
    print(emoji.emojize('\033[1;34mVOCÊ:\033[m :v: \033[1;30mVS\033[m '
                        ':v: \033[1;4;33m:COMPUTADOR\033[m', use_aliases=True))
    print(emoji.emojize('\n\033[1;31mEMPATE \033[m:ok_hand:', use_aliases=True))
