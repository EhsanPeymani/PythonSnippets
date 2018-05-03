temperature = 22
day = 'Monday'

print('{0}\'s highest temperature is predicted to be {1}.'.format(day, temperature))


# using dictionary and unpacking
data = dict(temperature=22, day='Monday')
print('{day}\'s highest temperature is predicted to be {temperature}.'.format(**data))


# using variables
print('{DAY}\'s highest temperature is predicted to be {TEMP}.'.format(TEMP=temperature, DAY=day))