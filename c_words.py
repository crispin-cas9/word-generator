# caemattos word generator
# ae = ash

# some goals:
# make probability of some letters higher
# have a dictionary that classes consonants as fricatives or stops (or other)
# make it less likely for one sound to be repeated throughout a word
# if the last syllable ends with two consonants, make it so that the next syllable has no onset (starts with a vowel)

# important! in a syllable: onset = starting consonants, nucleus = middle vowels, coda = ending consonants

import random as rd

def gen_syll():

	vowels = ["a", "ae", "e", "i", "o", "u"]
	consonants = ["d", "dd", "c", "cc", "f", "ff", "h", "hh", "l", "ll", "m", "n", "nn", "p", "pp", "r", "rr", "s", "ss", "t", "tt", "y", "yy", "z", "zz"]
	
	# I don't necessary classify consonants correctly here -- for example, LL is not a fricative and Y is, but I'm classifying them this way to make it all easier for myself. 
	
	consonants = {"d": ["fric", 1], "dd": "fric", "c": "stop", "cc": "stop", "f": "fric", "ff": "fric", "h": "other", "hh": "other", "l": "other", "ll": "fric", "m": "other", "n": "other", "nn": "other", "p": "stop", "pp": "stop", "r": "fric", "rr": "other", "s": "fric", "ss": "fric", "t": "stop", "tt": "stop", "y": "other", "yy": "other", "z": "fric", "zz": "fric"}
	
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
