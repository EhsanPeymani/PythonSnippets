# talkpython.fm
data = dict(year=2000, country='Norway', title='Nice', duration='120 min')


# asking for None when value key is non existence
print('rating:', data.get('rating'))
print('rating:', data.get('rating', 'NA'))



# use deafultdictionary for returning default value for any missing key
import collections

new_data = collections.defaultdict(lambda: 'Missing', data)
print(new_data)
print('rating:', new_data['rating'])
