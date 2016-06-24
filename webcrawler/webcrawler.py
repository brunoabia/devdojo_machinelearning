

import tweepy
import csv
import time

# CHAVES DE ACESSO FORNECIDAS NO SITE DO TWITTER
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# bruno.abia@gmail.com


# Autenticando o acesso
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

# Onde os dados coletados serão salvos
arq   = csv.writer(open("base_teste.csv","w"))
arq2  = open("base_teste_json.json","w")


row=[]
# api.search é a API que estamos utilizando. O q é onde vc deve informar qual termo quer consultar. Since e Until são as datas
# lang é o parâmetro do idioma
statuses = tweepy.Cursor(api.search,q='#orlando', since='2016-06-22', until='2016-06-23',lang='en').items()




while True:
    try:
        # Lendo os tweets
        status = statuses.next()
        # capturando só alguns parametros
        row=str(status.user.screen_name),str(status.created_at),str(status.text),status.geo
        # Escrevendo no CSV
        arq.writerow(row)
        # Salvando o JSON
        arq2.write(str(status))
        arq2.write("\n")

        exit()

    except tweepy.TweepError:
        # Devido a limitação a cada 3200 tweets é necessário esperar 15 minutos
        print("wait 15 minutes...")
        time.sleep(60*15)
        continue
    except StopIteration:
        print("Acabou!!")
        break
