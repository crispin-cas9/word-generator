# caemattos word generator
# ae = ash

# THE RULES
# (C)V(C) syllable structure, no coda at the end of a word

import random as rd
from numpy.random import choice


# converts weight numbers so that they sum to 1

def convert(list):
	newlist = []
	for n in list:
		new = n/float(sum(list))
		newlist.append(new)
	return newlist


def gen_syll(num, prevnt):
	
	# num is the number syllable it is -- either 'middle' or 'last'. A middle syllable has the structure (C)V(C); the last syllable is (C)V
	# prevnt = previous nucleus type
	
	# d = diphthong, v = vowel
	
	voweldict = {"a": [6, 'v'], "ae": [5, 'v'], "e": [5, 'v'], "i": [6, 'v'], "o": [5, 'v'], "u": [4, 'v'], "ai": [0.5, 'd'], "ei": [0.5, 'd'], "oi": [0.5, 'd'], "ui": [0.5, 'd']}
	
	# the numbers in the dict are weights
	
	consonantdict = {"d": 5, "dd": 4, "c": 6, "cc": 3, "f": 5, "ff": 3, "h": 3, "hh": 2, "l": 4, "ll": 4, "m": 5, "n": 6, "nn": 2, "p": 3, "pp": 2, "r": 5, "rr": 2, "s": 5, "ss": 3, "t": 5, "tt": 3, "y": 4, "yy": 2, "z": 4, "zz": 3}
	
	consonants = sorted(consonantdict.keys())
	weights = []
	vowels = sorted(voweldict.keys())
	vweights = []
		
	for letter in consonants:
		weights.append(consonantdict[letter])
	
	for letter in vowels:
		vweights.append(voweldict[letter][0])
	
	weights = convert(weights)
	vweights = convert(vweights)
		
	syll = ""

	
	# onset
	
	is_onset = rd.randint(0,2)
	
	if prevnt == 'd':
		is_onset = 1

	if is_onset == 1 or is_onset == 2:
		onset = choice(consonants, p=weights)
		syll = syll + onset
		consonantdict[onset] = 2
	
	
	# nucleus
	
	nucleus = choice(vowels, p=vweights)
	syll = syll + nucleus
	if voweldict[nucleus][1] == 'd':
		nucleustype = 'd'
	else:
		nucleustype = 'v'
	
	
	# coda
	# picking from 4 numbers to make the probability of a coda smaller
	
	if num == 'last':
		is_coda = 0
	else:
		is_coda = rd.randint(0,3)
	
	
	no = ["h", "hh", "y", "yy"]
	
	endcons = []
	endweights = []
	
	for letter in consonants:
		if letter not in no:
			endcons.append(letter)
	
	for key in consonants:
		if key in endcons:
			endweights.append(consonantdict[key])
	
	endweights = convert(endweights)
	 
	
	if is_coda == 1:
		syll = syll + choice(endcons, p=endweights)
	
	
	return [syll, nucleustype]


# generates a word made from syllables

def generate():
 	
 	nucleustype = 'v'
 	word = ""
 	syllnum = rd.randint(1,2)
 	
 	for x in range(syllnum):
 		
 		output = gen_syll('middle', nucleustype)
		
		syll = output[0]
		nucleustype = output[1]
		
		word = word + syll
 	
 	word = word + gen_syll('last', nucleustype)[0]
 	
 	return word


wordlist = []

for y in range(0,11):
	wordlist.append(generate())

print wordlist
