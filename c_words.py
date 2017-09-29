# caemattos word generator
# ae = ash; ee = schwa

import random as rd

vowels = ["a", "ae", "e", "ee", "i", "o", "u"]
consonants = ["d", "dd", "c", "cc", "f", "ff", "h", "hh", "l", "ll", "m", "n", "nn", "p", "pp", "r", "rr", "s", "ss", "t", "tt", "y", "yy", "z", "zz"]


def gen_syll():

	syll = ""

	# is there an onset? 0 = no; 1 = yes
	
	is_onset = rd.randint(0,1)
	coda_num = rd.randint(1,2)

	if is_onset == 1:
		syll = syll + rd.choice(consonants)
	
	# nucleus
	
	syll = syll + rd.choice(vowels)
	
	# coda. fix later!!
	
	syll = syll + rd.choice(consonants)
	
	if coda_num == 2:
		syll = syll + rd.choice(consonants)
	
	return syll


def generate():
	
	word = ""
	syllnum = rd.randint(1,4)
	
	for x in range(syllnum):
		word = word + gen_syll()
	
	return word


for y in range(0,11):
	print generate()
