# talkpython

# idea is to learn a bit about requests package
import requests

title_text = input('Enter a title search: ')
url = 'http://www.omdbapi.com/?i=tt3896198&apikey=656a5887&r=json&s={}'.format(title_text)

try:
    print(url)
    resp = requests.get(url)

    if resp.status_code != 200:
        print('Status Code {}'.format(resp.status_code))
    else:
        data = resp.json()

        for movie in data['Search']:
            print('* {}'.format(movie['Title']))

    resp.close()

except Exception as e:
    print('something goes wrong: {}'.format(e))