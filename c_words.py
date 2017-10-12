# caemattos word generator
# ae = ash

# some goals:
# make probability of some letters higher
# have a dictionary that classes consonants as fricatives or stops (or other)
# make it less likely for one sound to be repeated throughout a word
# if the last syllable ends with two consonants, make it so that the next syllable has no onset (starts with a vowel)

# important! in a syllable: onset = starting consonants, nucleus = middle vowels, coda = ending consonants

import random as rd
from numpy.random import choice

def gen_syll():

	vowels = ["a", "ae", "e", "i", "o", "u"]
	consonants = ["d", "dd", "c", "cc", "f", "ff", "h", "hh", "l", "ll", "m", "n", "nn", "p", "pp", "r", "rr", "s", "ss", "t", "tt", "y", "yy", "z", "zz"]
	
	# I don't necessary classify consonants correctly here -- for example, LL is not a fricative and Y is, but I'm classifying them this way to make it all easier for myself
	
	consonants2 = {"d": ["fric", 0.05], "dd": ["fric", 0.03], "c": ["stop", 0.05], "cc": ["stop", 0.03], "f": ["fric", 0.05], "ff": ["fric", 0.03], "h": ["other", 0.05], "hh": ["other", 0.03], "l": ["other", 0.04], "ll": ["fric", 0.04], "m": ["other", 0.04], "n": ["other", 0.05], "nn": ["other", 0.03], "p": ["stop", 0.05], "pp": ["stop", 0.03], "r": ["fric", 0.05], "rr": ["other", 0.03], "s": ["fric", 0.05], "ss": ["fric", 0.03], "t": ["stop", 0.05], "tt": ["stop", 0.03], "y": ["other", 0.05], "yy": ["other", 0.03], "z": ["fric", 0.05], "zz": ["fric", 0.03]}
	
	frics = ["d", "dd", "f", "ff", "ll", "r", "s", "ss", "z", "zz"]
	stops = ["c", "cc", "p", "pp", "t", "tt"]

	syll = ""

	# is there an onset? 0 = no; 1 = yes
	is_onset = rd.randint(0,1)
	
	# are there two consonants in the coda? picking from 4 numbers to make the probability of 2 consonants smaller
	coda_num = rd.randint(1,6)

	if is_onset == 1:
		syll = syll + rd.choice(consonants)
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	no = ["h", "hh", "y", "yy"]
	
	for letter in no:
		consonants.remove(letter)
	
	# coda
	
	if coda_num == 2:
		fric = rd.choice(frics)
		for letter in stops:
			if len(letter) != len(fric) and letter != "r":
				stops.remove(letter)
		syll = syll + fric + rd.choice(stops)
	else:
		syll = syll + rd.choice(consonants)
	
	return syll


def generate():
	
	word = ""
	syllnum = rd.randint(1,3)
	
	for x in range(syllnum):
		word = word + gen_syll()
	
	return word


for y in range(0,11):
	print generate()
