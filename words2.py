# caemattos word generator
# ae = ash

# THE RULES
# (C)V(C) syllable structure with no coda at the end of a word

import random as rd
from numpy.random import choice


# converts weight numbers so that they sum to 1

def convert(list):
	newlist = []
	for n in list:
		new = n/float(sum(list))
		newlist.append(new)
	return newlist


def gen_syll():
		
	vowels = ["a", "ae", "e", "i", "o", "u"]
	
	# the numbers in the dict are weights
	
	consonantdict = {"d": 5, "dd": 4, "c": 6, "cc": 3, "f": 5, "ff": 3, "h": 3, "hh": 2, "l": 4, "ll": 4, "m": 5, "n": 6, "nn": 2, "p": 3, "pp": 2, "r": 5, "rr": 2, "s": 5, "ss": 3, "t": 5, "tt": 3, "y": 4, "yy": 2, "z": 4, "zz": 3}
	
	consonants = consonantdict.keys()
	weights = []
		
	for letter in sorted(consonantdict.keys()):
		weights.append(consonantdict[letter])
	
	weights = convert(weights)
		
	syll = ""

	
	# onset
	
	is_onset = rd.randint(0,1)

	if is_onset == 1:
		onset = choice(consonants, p=weights)
		syll = syll + onset
		consonantdict[onset] = 2
	
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	
	# coda
	# picking from 4 numbers to make the probability of a coda smaller
	
	is_coda = rd.randint(0,3)

	if is_coda == 1:
		coda = choice(consonants, p=weights)
		syll = syll + coda
	
	
	return syll


# generates a word made from syllables

def generate():
 	
 	word = ""
 	syllnum = rd.randint(1,3)
 	
 	for x in range(syllnum):
 		word = word + gen_syll()
 	
 	return word


wordlist = []

for y in range(0,11):
	wordlist.append(generate())

print wordlist
