import tweepy as tw
import time
import credentials as config
import csv
import keyboard


file_name = 'tweets.csv'
my_file = open(file_name, 'w', encoding='utf-8')
fieldnames = ['seguidores', 'seguidos', 'tweets']
wr = csv.writer(my_file)
wr.writerow(fieldnames)
# Authenticate to Twitter
client = tw.Client(bearer_token=config.bearerToken)
# query
query = 'futbol -is:retweet'


# search_recent_tweets
"""response = client.search_recent_tweets(
    query=query, max_results=10, tweet_fields=['author_id', 'created_at', 'text', 'source', 'lang', 'geo', 'public_metrics'],)"""


"""for tweets in response.data:
    print('User id: ', tweets.author_id)
    print('Dispositive: ', tweets.source)
    print('language: ', tweets.lang)
    print('Geo: ', tweets.geo)
    print('Create at: ', tweets.created_at)
    print('Public metrics: ', tweets.public_metrics)
    print('Text:', tweets.text)
    print('--------------------------------------------------------')"""

def data():
  response = client.get_user(id=1303576011716595712, user_fields=['created_at', 'description', 'entities', 'id', 'location',
                           'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'])
  print('Numero de seguidores: ',
      response.data.public_metrics['followers_count'])
  print('Numero de seguidos: ',
        response.data.public_metrics['following_count'])
  print('Numero de tweets: ',
        response.data.public_metrics['tweet_count'])
  with open('tweets.csv', 'w') as csvfile:
      fieldnames = ['seguidores', 'seguidos', 'tweets']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      seguidores = response.data.public_metrics['followers_count']
      seguidos = response.data.public_metrics['following_count']
      twee = response.data.public_metrics['tweet_count']
      writer.writeheader()
      writer.writerow({'seguidores': seguidores,
                       'seguidos': seguidos, 'tweets': twee})

      #base de datos


  my_file.close()



while True:
    data()
    time.sleep(10)
    keyboard.press_and_release("F5")





"""response = client.get_users_following(id=1303576011716595712, user_fields=['created_at', 'description', 'entities', 'id', 'location',
                                                                           'name', 'pinned_tweet_id', 'profile_image_url', 'protected', 'public_metrics', 'url', 'username', 'verified', 'withheld'])
print('-----------------------------------')
for user in response.data:
    print('Nombre: ', user.username)
    print('Id: ', user.id)
    print('-----------------------------------')
    my_file.write(str(user.username) + ';' + str(user.id) + '\n')

my_file.close()"""
