import json, requests

SERVER_URL = "http://"

def setContact(name):
  print('\nBoooa {}...\nQue tal comecar pelo Whats?\n'.format(name))
  cellphone = input('Manda o ZAP ~> ')
  print('Se você não tiver ou apenas não quer passar as proximas infos pq e anti-social é só apertar ENTER como se não houvesse o amanhã')
  facebook = input('\nLegal, manda o Facebook tbm ~> ')
  github = input('\nPassa o GitHub ~> ')
  twitter = input('\nTwitter, pq a gnt precisa desabafar ~> ')
  email = input('\nVocê quer receber uma copia dessas informações? Se sim, manda o email ~> ')
  return {
    "name": name,
    "cellphone": cellphone,
    "facebook": facebook,
    "github": github,
    "twitter": twitter,
    "email": email
  }

def sendEmail(infos):
  r = requests.post(SERVER_URL, data=json.dumps(infos))
  r.text
  r.status_code

print('Oooi... Tudo bem?\nVou te ajudar a entrar em contato com esse ser lindo!!!\nMas primeiro...')
name = input('Qual seu nome? ;] ~> ')
print('\nOlá {}. Bom agora que já tenho seu nome o que acha\nde me passar o restante do seu contato?\n'.format(name))
opc0 = input('s para SIM e n para NÃO ~> ')
if opc0 == 's':
  sendEmail(setContact(name))
else:
  print('Poxa, tudo bem! :]\nObrigado mesmo assim...')
