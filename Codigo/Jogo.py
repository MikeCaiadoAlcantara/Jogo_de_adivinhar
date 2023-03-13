from random import randint
from time import sleep

print("\033[7;32m_-_-\033[m" * 18)
print("\033[1;32mVou pensar em um número entre 0 e 5 tente adivinhar...\033[m".center(75))
print("\033[7;32m_-_-\033[m" * 18)
sleep(1)
n = int(input("\033[1;32mEm que número eu pensei?\033[m\n"))
print("\033[0;30;41mPROCESSANDO...\033[m")
sleep(2)
nSecreto = randint(0, 5) # faz o computador pensar
if n != nSecreto:
	print("\033[1;31mERROU!!!\033[m \033[32mpensei no numero {}\033[m".format(nSecreto))
else:
	print("\033[1;34mACERTOU\033[m, \033[32mParabéns você conseguiu me vencer!!!\033[m")