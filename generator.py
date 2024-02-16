#random word+num generator that im trying to make hh
# generate random word
import random_word
import numpy.random
from random_word import RandomWords
x = RandomWords()
random_word = x.get_random_word()
print(random_word)
# generate random number ]100;1000[
import numpy as np
r = np.random.RandomState()
np.random = r
random_int = np.random.randint(100,1000)
print(random_int)
# combining them
the_random = random_word + str(random_int)
print(the_random)

