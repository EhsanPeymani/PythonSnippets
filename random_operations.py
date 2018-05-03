import random

# choose a character randomly
s = 'abcdefghijklmnopqrstuvwxyz1234567890'


# non-pythonic approach for randomly picking character
def pick_randomly_nonpythonic(text: str):
    index = random.randint(0, len(text)-1)
    return text[index]

if s:
    print(pick_randomly_nonpythonic(s))


# pythonic approach
if s:
    print(random.choice(s))



# shuffling the string s using random.sample
shuffled_list = random.sample(s, len(s))
print(''.join(shuffled_list))



# sampling 5 characters from the string s
sampled = random.sample(s, 5)
print('sampled', sampled)




# shuffling the string s using random.shuffle
# point 1: shuffle it in place
# point 2: it requires list
s_list = list(s)
random.shuffle(s_list)
print(''.join(s_list))


