import random

numeros = list(range(1,11))
num_escolhido = random.choice(numeros)

def randomizar():
  global num_escolhido
  num_escolhido = random.choice(numeros)

def jogar_novamente():
  resposta_jogarnovamente = input('Jogar novamente? Y/N\n\n')
  if resposta_jogarnovamente in ['Y','y']:
    randomizar()
    dice_roll()
  elif resposta_jogarnovamente in ['N','n']:
    print('Tudo bem! Obrigado por jogar!')
  else:
    jogar_novamente()

def verificar(x):
  if int(x) > 10 or int(x) <= 0:
    print('Somente números de 1 a 10!')
    dice_roll()
  elif int(x) == num_escolhido:
    print('Acertou!')
    jogar_novamente()
  else:
    print('Errou! O número era ' + str(num_escolhido))
    jogar_novamente()


def dice_roll():
  escolha = input('Escolha um número!\n')
  try:
    int(escolha)
  except:
    if type(escolha) == str:
      print('Você tem que escolher um integro de 1 a 10 e não uma string!')
      dice_roll()
  verificar(int(escolha))

print('Tente adivinhar de 1 a 10 o número escolhido!\n')
dice_roll()
