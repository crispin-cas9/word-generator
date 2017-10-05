# caemattos word generator
# ae = ash (no schwas yet...)

# important! in a syllable: onset = starting consonants, nucleus = middle vowels, coda = ending consonants

import random as rd

def gen_syll():

	vowels = ["a", "ae", "e", "i", "o", "u"]
	consonants = ["d", "dd", "c", "cc", "f", "ff", "h", "hh", "l", "ll", "m", "n", "nn", "p", "pp", "r", "rr", "s", "ss", "t", "tt", "y", "yy", "z", "zz"]
	
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
