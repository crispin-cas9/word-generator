# caemattos
# ae = ash; ee = schwa

import random as rd

vowels = ["a", "ae", "e", "ee", "i", "o", "u"]
consonants = ["d", "dd", "c", "cc", "f", "ff", "h", "hh", "l", "ll", "m", "n", "nn", "p", "pp", "r", "rr", "s", "ss", "t", "tt", "y", "yy", "z", "zz"]

def generate():

	length = rd.randint(2,5)

	l = length - 1
	word = ""

	# is there a vowel at the beginning?
	cfirst = rd.randint(0,1)

	if cfirst == 1:
		x = rd.choice(consonants)
		word = word + x

	for x in range(0,l):
		x = rd.choice(vowels)
		word = word + x
		x = rd.choice(consonants)
		word = word + x
	
	return word

for y in range(0,11):
	print generate()