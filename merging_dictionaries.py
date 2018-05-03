# partly taken from talkpython.fm
temperatures = [20, 22, 19, 20, 17]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# creating dictionary from 2 lists
temp_dict = dict(zip(weekdays, temperatures))
print('temp_dict', temp_dict)



# merging dictionaries
route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}


# non-pythonic
m1 = {}
for k in query:
    m1[k] = query[k]
for k in post:
    m1[k] = post[k]
for k in route:
    m1[k] = route[k]



# classic pythonic
m2 = query.copy()
m2.update(post)
m2.update(route)



# dictionary comprehensions
m3 = {k: v for item in [query, post, route] for k, v in item.items()}



# pthon > 3.4
m4 = {**query, **post, **route}
print(m4)